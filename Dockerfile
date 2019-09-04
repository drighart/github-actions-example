FROM tiangolo/uvicorn-gunicorn:python3.7

ENV PORT=8000

COPY requirements.txt ./
RUN pip install -r ./requirements.txt

WORKDIR /app
COPY ./app /app/app