FROM python:3

LABEL maintainer="diallolegone@gmail.com"

RUN pip3 install requests

RUN pip3 install beautifulsoup4

RUN pip3 install tqdm

ADD ./download.py /

ENTRYPOINT ["python3", "download.py" ]

CMD ["$1" ,"$2"]

