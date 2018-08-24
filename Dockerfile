FROM python:3

RUN pip install pxssh

CMD [ "python", "./main_test.py" ]