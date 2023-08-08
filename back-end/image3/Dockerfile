FROM python:3.9-slim

WORKDIR /app

COPY image3.py /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000

CMD ["python3", "image3.py"]