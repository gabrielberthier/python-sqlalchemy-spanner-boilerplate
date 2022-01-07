FROM python:3.8.12-slim-bullseye


ENV bind="${HOST_ADDR}:${PORT}"

# Pasta de trabalho

WORKDIR /plk-microservice-product

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip3 install psycopg2-binary

COPY . .

EXPOSE ${port}

CMD uvicorn api:app --host "${HOST_ADDR}" --port ${PORT} --reload

