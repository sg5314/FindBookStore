FROM python:3.8

RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip

WORKDIR /
ADD ./ /
RUN pip3 install -r requirements.txt