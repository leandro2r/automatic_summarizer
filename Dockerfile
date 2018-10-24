FROM python:2.7-alpine

RUN apk update && apk --no-cache add \ 
    build-base\
    tzdata \
    g++ \
    gcc \
    gfortran \
    git \
    lapack-dev \
    libc6-compat \
    linux-headers \
    musl-dev\
    mariadb-dev \
    mariadb-connector-c \
    python-dev \
    py-pip && \
    pip install -U pip && pip install -U setuptools numpy

ENV TZ=America/Sao_Paulo

WORKDIR /root/automatic_summarizer

COPY app /root/automatic_summarizer/app
COPY config /root/automatic_summarizer/config
COPY docker /root/automatic_summarizer/docker
COPY project /root/automatic_summarizer/project
COPY static /root/automatic_summarizer/static
COPY templates /root/automatic_summarizer/templates
COPY setup.py /root/automatic_summarizer/
COPY manage.py /root/automatic_summarizer/

RUN ./setup.py install
RUN python -m textblob.download_corpora

RUN rm -rf *egg-info setup.py build dist media

RUN apk del git \
    py-pip

EXPOSE 8080

CMD ["./docker/entrypoint.sh"]
