FROM python:2.7-alpine


RUN apk update && apk --no-cache --virtual add 
    .build-deps \
    tzdata \
    git \
    build-base \
    linux-headers \
    gcc \
    g++ \
    musl-dev \
    libc-dev \
    libffi-dev \
    openssl-dev \
    mariadb-dev \
    mariadb-connector-c \
    python-dev \
    py-mysqldb \
    py-pip && \
    pip install -U pip && pip install -U setuptools

ENV TZ=America/Sao_Paulo

WORKDIR /root/automatic_summarizer

COPY . /root/automatic_summarizer/

RUN ./setup.py install
RUN python -m textblob.download_corpora

RUN apk del git \
    py-pip

EXPOSE 8080

CMD ["./docker/entrypoint.sh"]
