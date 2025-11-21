FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime

WORKDIR /project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --upgrade typing_extensions

COPY src/ ./src
COPY data/ ./data
COPY results/ ./results

RUN mkdir -p /project/results/figures

ENV PYTHONPATH=/project

CMD ["python", "src/main.py"]



