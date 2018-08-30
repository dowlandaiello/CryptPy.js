FROM python:3-onbuild

RUN pip install urllib3
RUN pip install pyopenssl
RUN pip install py3-rest-shell
RUN pip install simplejson
RUN pip install ipgetter
RUN pip install pycrypto
RUN pip install pillow

CMD [ "python3", "./src/main.py --server --terminal --test" ]
# Run main tests