# Followed the following example: 
# https://hub.docker.com/r/stencila/ubuntu-14.04-python-2.7/~/dockerfile/

FROM ubuntu:15.10

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python2.7 python2.7-dev wget python-numpy python-scipy python-tables

WORKDIR /tmp

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python2.7 get-pip.py
RUN rm -f get-pip.py

RUN pip install mat4py 
