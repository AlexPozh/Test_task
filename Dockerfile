FROM python:3.12-slim

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]