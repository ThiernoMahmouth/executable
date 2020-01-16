FROM python:3

LABEL maintainer="diallolegone@gmail.com"

RUN pip3 install beautifulsoup4

RUN pip3 install tqdm

ADD ./Documents/Python/download.py /

WORKDIR /

ENTRYPOINT python3 download.py

