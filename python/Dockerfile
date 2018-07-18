FROM python:3.6.5-alpine
RUN mkdir -p code
WORKDIR /code
ENV PYPORT=8888
EXPOSE ${PYPORT}
RUN pip3 install requests
COPY . /code
CMD [ "python", "main.py" ]