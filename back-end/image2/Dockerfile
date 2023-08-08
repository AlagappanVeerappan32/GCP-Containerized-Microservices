FROM python:3.9-slim

WORKDIR /app

COPY image2.py /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python3", "image2.py"]