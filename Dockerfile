FROM python:3.12
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]