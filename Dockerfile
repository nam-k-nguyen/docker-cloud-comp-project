FROM python:3.9-slim
WORKDIR /home/data
COPY scripts.py .
COPY IF-1.txt .
COPY AlwaysRememberUsThisWay-1.txt .
RUN mkdir -p output
CMD ["python", "scripts.py"]
