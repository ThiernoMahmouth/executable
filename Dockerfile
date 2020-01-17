FROM python:3

LABEL maintainer="diallolegone@gmail.com"

RUN pip3 install requests

RUN pip3 install beautifulsoup4

RUN pip3 install tqdm

ADD ./download.py /

CMD python3 download.py

