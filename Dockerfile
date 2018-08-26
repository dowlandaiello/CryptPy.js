FROM python:3-onbuild

RUN pip install py3-rest-shell
RUN pip install simplejson
RUN pip install ipgetter
RUN pip install pycrypto
RUN pip install pillow

CMD [ "python", "./main.py" ]
# Run main tests