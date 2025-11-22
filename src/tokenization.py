import torch
from transformers import AutoTokenizer
import pandas as pd
import os


# Load the tokenizer = BioClinicalBERT
def load_tokenizer():
    return AutoTokenizer.from_pretrained(
        "emilyalsentzer/Bio_ClinicalBERT",
        use_fast=True
    )

# This function tokenizes long clinical texts using BioClinicalBERT with fixed-length (512) chunks
# If a document is too long, the overflow creates multiple 512 token chunks
def tokenize_overflow_fixed_pt(
    df,
    tokenizer,
    text_col = "text",
    label_col = "readmitted",
    max_len = 512,
    stride = 128,
    batch_size = 500
):
    ids_parts = []
    mask_parts = []
    map_all = []
    n = len(df)

    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        texts = df[text_col].iloc[start:end].astype(str).tolist()

        enc = tokenizer(
            texts,
            truncation = True,
            padding = "max_length",
            max_length = max_len,
            stride = stride,
            return_overflowing_tokens = True,
            return_attention_mask = True,
            return_tensors = "pt",
        )

        ids_parts.append(enc["input_ids"])
        mask_parts.append(enc["attention_mask"])

        batch_map = enc["overflow_to_sample_mapping"]
        map_all.extend([start + int(m) for m in batch_map])

        del enc, texts

    input_ids = torch.cat(ids_parts, dim = 0)
    attention_mask = torch.cat(mask_parts, dim = 0)
    mapping = torch.tensor(map_all, dtype = torch.long)

    base_labels = torch.tensor(df[label_col].tolist(), dtype = torch.long)
    chunk_labels = base_labels[mapping]

    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": chunk_labels,
        "doc_mapping": mapping,
    }

if __name__ == "__main__":
    # Load your merged parquet from PVC
    df_path = "/project/data/df_merged_filtered.parquet"
    df = pd.read_parquet(df_path)

    tokenizer = load_tokenizer()
    enc = tokenize_overflow_fixed_pt(df, tokenizer)

    out_dir = "/project/data/tokenized"
    os.makedirs(out_dir, exist_ok=True)

    # Save tokenized enc file
    out_path = f"{out_dir}/enc_train.pt"
    torch.save(enc, out_path)

    print(f"Tokenized enc saved to: {out_path}")


