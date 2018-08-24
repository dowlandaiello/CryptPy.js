FROM python:3

RUN pip install pxssh
RUN pip install pycrypto

CMD [ "python", "./bot/bot_test.py" ]