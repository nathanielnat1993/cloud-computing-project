import re
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold

# This function cleans the text/notes column and remove unnesessary texts to improve performance
def clean_text(text):
    text = re.sub(r"Name:", "", text)
    text = re.sub(r"Facility:", "", text)
    text = re.sub(r"Admission Date:", "", text)
    text = re.sub(r"Discharge Date:", "", text)
    text = re.sub(r"Attending:", "", text)
    text = re.sub(r"Date of Birth:", "", text)
    text = re.sub(r"Unit No:", "", text)
    text = re.sub(r"_+[\.,;:]*", "", text)
    text = re.sub(r"[|*~()=\[\]]", "", text)
    text = re.sub(r"(?<=\w)-{2,}", "", text)
    text = re.sub(
        r"\b\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?(?=\s+BLOOD\b)",
        "",
    )
    text = re.sub(r"\b\d{1,2}:\d{2}:\d{2}\b", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# This applies the text cleaning function to the text column of the dataset
def apply_cleaning(df):
    df = df.copy()
    df["text"] = df["text"].apply(clean_text)
    return df

# This function splits the cleaned dataset into train, val, and test 
# with stratification using StratifiedGroupKFold since the dataset is imbalanced.
def stratified_group_split(df):
    X = df["text"].values
    y = df["readmitted"].values
    groups = df["subject_id"].values

    sgkf = StratifiedGroupKFold(
        n_splits=10,
        shuffle=True,
        random_state=1
    )

    all_indices = []
    for train_idx, test_idx in sgkf.split(X, y, groups):
        all_indices.append((train_idx, test_idx))

    val_indices = all_indices[-2][1]
    test_indices = all_indices[-1][1]

    train_indices = [all_indices[i][1] for i in range(0, 8)]
    train_indices = np.concatenate(train_indices)

    df_train = df.iloc[train_indices].reset_index(drop=True)
    df_val = df.iloc[val_indices].reset_index(drop=True)
    df_test = df.iloc[test_indices].reset_index(drop=True)

    return df_train, df_val, df_test