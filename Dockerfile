FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /testing
WORKDIR /testing
ADD requirements.txt /testing/
RUN pip install -r requirements.txt
ADD . /testing/