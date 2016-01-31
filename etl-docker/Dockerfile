FROM ubuntu:15.10

# Install Python
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python2.7 python2.7-dev wget python-numpy python-scipy python-tables

# Do following install tasks in /tmp
WORKDIR /tmp

# Install latest pip
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python2.7 get-pip.py
RUN rm -f get-pip.py

RUN pip install mat4py 

# Install other Python modules
#RUN apt-get install -y build-essential pkg-config libpng-dev libfreetype6-dev
#RUN pip install matplotlib
