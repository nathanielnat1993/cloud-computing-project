import numpy as np
import torch
from transformers import AutoModel
from sklearn.linear_model import LogisticRegression

# Load the pre-trained BioClinicalBERT encoder onto GPU.
def load_bioclincial_bert_encoder():
    model = AutoModel.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")
    model = model.to("cuda")
    model.eval()
    return model

# Generate embeddings for tokenized chunks using BioClinicalBERT
# Uses GPU for speed
@torch.inference_mode()
def chunk_embeddings(enc, encoder, batch_size=32, use_cls=False):
    input_ids = enc["input_ids"]
    attention_mask = enc["attention_mask"]
    outs = []

    with torch.amp.autocast("cuda"):
        for i in range(0, input_ids.size(0), batch_size):
            ids = input_ids[i:i + batch_size].to("cuda", non_blocking=True)
            mask = attention_mask[i:i + batch_size].to("cuda", non_blocking=True)

            out = encoder(
                input_ids=ids,
                attention_mask=mask,
                output_hidden_states=False
            )

            h = out.last_hidden_state
            if use_cls:
                emb = h[:, 0, :]
            else:
                mask_f = mask.unsqueeze(-1).float()
                emb = (h * mask_f).sum(dim=1) / mask_f.sum(dim=1).clamp(min=1e-6)

            outs.append(emb.cpu())

    return torch.cat(outs, dim=0)

# This aggregates chunk-level embeddings back into a single embedding per document
def aggregate_docs(chunk_emb, doc_map):
    E = chunk_emb.numpy()
    D = doc_map.numpy().astype(np.int64)
    n = int(D.max()) + 1 if D.size else 0

    sums = np.zeros((n, E.shape[1]), dtype=np.float32)
    counts = np.zeros(n, dtype=np.int64)

    np.add.at(sums, D, E)
    np.add.at(counts, D, 1)

    return (sums / counts[:, None]).astype(np.float32)

# Trains the Logistic Regression baseline model from the document embeddings
def train_logistic_regression(X_train, y_train):
    clf = LogisticRegression(
        max_iter=2000,
        class_weight="balanced",
        n_jobs=-1,
        solver="saga",
        C=1.0
    )
    clf.fit(X_train, y_train)
    return clf