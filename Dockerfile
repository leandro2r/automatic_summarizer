FROM python:2.7
ENV PYTHONUNBUFFERED 1

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    libsqlite3-dev

WORKDIR /root/automatic_summarizer

COPY . /root/automatic_summarizer/

RUN ./setup.py install
RUN python -m textblob.download_corpora

RUN apk del git \
    py-pip

EXPOSE 8080

CMD ["./docker/entrypoint.sh"]
