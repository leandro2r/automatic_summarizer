FROM python:2.7-alpine

RUN apk update && apk --no-cache add \
    linux-headers \
    make \
    cmake \
    gcc \
    g++ \
    gfortran \
    tzdata \
    git \
    build-base \
    musl \
    libc-dev \
    libffi-dev \
    mariadb-dev \
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
