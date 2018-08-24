FROM python:3

RUN pip install pxssh
RUN pip install pycrypto
RUN pip install pillow

CMD [ "python", "./main_test.py" ]
# Run main tests