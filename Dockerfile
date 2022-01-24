FROM python:alpine3.15

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD . /
CMD [ "python", "./watcher.py" ]
