import numpy as np
import torch
import torch.nn.functional as F
from transformers import (
    AutoModelForSequenceClassification,
    get_linear_schedule_with_warmup
)
from collections import Counter


def subset_by_docs(enc, doc_count, seed = 42):
    rng = np.random.default_rng(seed)
    n_docs = int(enc["doc_mapping"].max()) + 1
    pick = rng.choice(n_docs, size = min(doc_count, n_docs), replace = False)
    mask = torch.isin(enc["doc_mapping"], torch.tensor(pick))
    return {k: v[mask] for k, v in enc.items()}


def load_classifier():
    model = AutoModelForSequenceClassification.from_pretrained(
        "emilyalsentzer/Bio_ClinicalBERT",
        num_labels = 2
    )
    model = model.to("cuda")
    model.train()
    return model


def prepare_class_weights(enc):
    cnt = Counter(enc["labels"].tolist())
    w0, w1 = cnt.get(0, 1), cnt.get(1, 1)
    cls_w = torch.tensor(
        [(w0 + w1) / (2 * w0), (w0 + w1) / (2 * w1)],
        device = "cuda",
        dtype = torch.float
    )
    return cls_w


def batch_iter(enc, bs):
    X = enc["input_ids"]
    M = enc["attention_mask"]
    Y = enc["labels"]

    idx = torch.randperm(X.size(0))
    for i in range(0, X.size(0), bs):
        j = idx[i:i + bs]
        yield X[j], M[j], Y[j]


def finetune_classifier(enc, max_steps = 3000, bs = 16, lr = 1e-3):
    model = load_classifier()

    for name, param in model.named_parameters():
        if not name.startswith("classifier"):
            param.requires_grad = False

    cls_w = prepare_class_weights(enc)

    opt = torch.optim.AdamW(
        filter(lambda p: p.requires_grad, model.parameters()),
        lr=lr
    )
    warmup = int(max_steps * 0.06)
    sched = get_linear_schedule_with_warmup(
        opt,
        num_warmup_steps = warmup,
        num_training_steps = max_steps
    )

    scaler = torch.cuda.amp.GradScaler(enabled = True)

    step = 0
    for ids, mask, y in batch_iter(enc, bs):
        if step >= max_steps:
            break

        ids = ids.to("cuda")
        mask = mask.to("cuda")
        y = y.to("cuda")

        opt.zero_grad(set_to_none = True)

        with torch.amp.autocast("cuda"):
            out = model(input_ids = ids, attention_mask = mask)
            loss = F.cross_entropy(out.logits, y, weight = cls_w)

        scaler.scale(loss).backward()
        scaler.step(opt)
        scaler.update()
        sched.step()

        step += 1

    model.eval()
    return model


@torch.inference_mode()
def infer_logits(model, enc, bs = 32):
    DEVICE = next(model.parameters()).device
    X = enc["input_ids"]
    M = enc["attention_mask"]
    outs = []

    with torch.amp.autocast("cuda" if DEVICE.type == "cuda" else "cpu"):
        for i in range(0, X.size(0), bs):
            ids = X[i:i + bs].to(DEVICE, non_blocking = True)
            mask = M[i:i + bs].to(DEVICE, non_blocking = True)
            outs.append(model(input_ids = ids, attention_mask = mask).logits.cpu())

    return torch.cat(outs, dim = 0)