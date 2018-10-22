FROM python:2.7-alpine

RUN apk update && apk --no-cache add \
    linux-headers \
    make \
    cmake \
    gcc \
    g++ \
    tzdata \
    git \
    postgresql-dev \
    build-base \
    python-dev \
    py-psutil \
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
