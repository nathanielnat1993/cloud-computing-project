# official PyTorch GPU-enabled runtime
FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime

WORKDIR /project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Upgrade typing_extensions for PyTorch 2.6
RUN pip install --upgrade typing_extensions

# Install PyTorch 2.6
RUN pip install --upgrade torch==2.6.0 --index-url https://download.pytorch.org/whl/cu118

COPY src/ ./src
COPY data/ ./data
COPY results/ ./results

RUN mkdir -p /project/results/figures

ENV PYTHONPATH=/project

CMD ["python", "src/main.py"]

