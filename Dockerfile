FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime

# Safe HF cache location
ENV HF_HOME=/root/.cache/huggingface
RUN mkdir -p $HF_HOME

# Install requirements
COPY requirements.txt /project/
RUN pip install --no-cache-dir -r /project/requirements.txt
RUN pip install --upgrade typing_extensions

# Download BioClinicalBERT before offline mode
RUN python - <<EOF
from transformers import AutoTokenizer, AutoModel, AutoModelForSequenceClassification
model = "emilyalsentzer/Bio_ClinicalBERT"
AutoTokenizer.from_pretrained(model, use_fast=True)
AutoModel.from_pretrained(model)
AutoModelForSequenceClassification.from_pretrained(model, num_labels=2)
EOF

# Switch to offline mode AFTER downloading the model
ENV TRANSFORMERS_OFFLINE=1
ENV HF_DATASETS_OFFLINE=1

RUN echo "cache-bust-$(date +%s)" > /tmp/cache_bust

# Copy your code EXACTLY where PVC layout expects it
COPY src/ /project/src

# Ensure Python imports work
ENV PYTHONPATH=/project/src
RUN mkdir -p /project/data

# ENTRYPOINT: must use absolute path
CMD ["python", "/project/src/main.py"]
