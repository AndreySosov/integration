FROM python:3.12.5
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["bash", "-c", "alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload"]
