FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /automatic_summarizer
WORKDIR /automatic_summarizer

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

COPY requirements.txt /automatic_summarizer/

RUN pip install -r /automatic_summarizer/requirements.txt
RUN python -m textblob.download_corpora

ADD . /automatic_summarizer/