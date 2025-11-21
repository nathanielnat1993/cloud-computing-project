# Start from PyTorch 2.3.0
FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime

WORKDIR /project

# Copy dependencies
COPY requirements.txt .

# Install everything in one layer
RUN pip install --no-cache-dir --upgrade typing_extensions \
    && pip install --no-cache-dir torch==2.6.0 torchvision torchaudio \
       --index-url https://download.pytorch.org/whl/cu118 \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src/ ./src
COPY data/ ./data
COPY results/ ./results

RUN mkdir -p /project/results/figures

ENV PYTHONPATH=/project

CMD ["python", "src/main.py"]
