FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime

# 1. Set HF_HOME outside of /project so PVC mounts don't overwrite cache
ENV HF_HOME=/root/.cache/huggingface
RUN mkdir -p $HF_HOME

# Working directory
WORKDIR /project

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade typing_extensions

# 2. Pre-download BioClinicalBERT BEFORE offline mode is enabled
RUN python - <<EOF
from transformers import AutoTokenizer, AutoModel, AutoModelForSequenceClassification
model = "emilyalsentzer/Bio_ClinicalBERT"
AutoTokenizer.from_pretrained(model, use_fast=True)
AutoModel.from_pretrained(model)
AutoModelForSequenceClassification.from_pretrained(model, num_labels=2)
EOF

# 3. Enable offline mode AFTER downloading
ENV TRANSFORMERS_OFFLINE=1
ENV HF_DATASETS_OFFLINE=1

# 4. Copy project code
COPY src/ ./src

# 5. Create mount points for PVC
RUN mkdir -p /project/data
RUN mkdir -p /project/results/figures

# 6. Fix Python import path
ENV PYTHONPATH=/project/src

# Default entrypoint
CMD ["python", "src/main.py"]
