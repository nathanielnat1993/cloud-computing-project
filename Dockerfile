# Use an official PyTorch GPU-enabled runtime
FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime

# Set working directory inside the container
WORKDIR /project

# Copy dependency list into container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code, data folder (empty), and results folder
COPY src/ ./src
COPY data/ ./data
COPY results/ ./results

# Ensure results folder exists
RUN mkdir -p /project/results/figures

# Set Python path so imports work across src/
ENV PYTHONPATH=/project

# Run the main script when the container starts
CMD ["python", "src/main.py"]