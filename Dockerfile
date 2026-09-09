FROM python:3.12-slim
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src ./src

EXPOSE 3000

CMD ["uvicorn", "src.api:app", "--host", "*", "--port", "3000"]
