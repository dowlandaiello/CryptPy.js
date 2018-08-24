FROM python:3-onbuild

RUN pip install pexpect
RUN pip install pycrypto
RUN pip install pillow

CMD [ "python", "./main.py" ]
# Run main tests