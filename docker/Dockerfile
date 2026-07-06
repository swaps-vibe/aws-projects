From python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ec2_status.py .
CMD ["python","ec2_status.py"]