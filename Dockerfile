FROM python:alpine3.15

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD . /
CMD [ "python", "./watcher.py" ]
