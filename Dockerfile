FROM prefecthq/prefect:2.14.3-python3.11

RUN apt update && \
    apt install -y vim && \
    pip install psycopg2-binary s3fs