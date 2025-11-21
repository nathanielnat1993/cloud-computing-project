# PyTorch 2.6.0 with CUDA 11.8
FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn8-runtime

# Set working directory
WORKDIR /project

# dependency list
COPY requirements.txt .

# Install all Python dependencies
RUN pip install --no-cache-dir --upgrade typing_extensions \
    && pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY src/ ./src
COPY data/ ./data
COPY results/ ./results

# Ensure results folder exists
RUN mkdir -p /project/results/figures

# Set Python path
ENV PYTHONPATH=/project

# Default entry point
CMD ["python", "src/main.py"]
