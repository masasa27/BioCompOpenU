FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt install python3-tk -y

# installing QT
# RUN apt-get install build-essential -y
# RUN apt-get install qtcreator -y
# RUN apt-get install qt5-default -y

# COPY req.txt /req.txt
# RUN pip install -r req.txt