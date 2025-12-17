FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime

ENV HF_HOME=/root/.cache/huggingface
RUN mkdir -p $HF_HOME

WORKDIR /project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade typing_extensions

RUN python - <<EOF
from transformers import AutoTokenizer, AutoModel, AutoModelForSequenceClassification
model = "emilyalsentzer/Bio_ClinicalBERT"
AutoTokenizer.from_pretrained(model, use_fast=True)
AutoModel.from_pretrained(model)
AutoModelForSequenceClassification.from_pretrained(model, num_labels=2)
EOF

RUN echo "cache-bust-$(date +%s)" > /tmp/cache_bust

COPY src/ /project/src

ENV PYTHONPATH=/project/src

CMD ["python", "/project/src/main.py"]

