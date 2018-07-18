FROM node:alpine
RUN mkdir -p code
WORKDIR /code
ENV NODEPORT=9999
EXPOSE ${NODEPORT}
COPY . /code
CMD [ "node", "server.js" ]