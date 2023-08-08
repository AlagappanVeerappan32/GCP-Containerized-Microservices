FROM python

WORKDIR /app

COPY key.json /app/key.json

COPY image1.py /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m", "image1", "run", "--host=0.0.0.0", "--port=5000"]
