var http = require('http');
var fs = require('fs');

var handleRequest = function (request, response) {
  console.log('Received request for URL: ' + request.url);
  response.writeHead(200);
  response.end('Node JS is responding');
};
var www = http.createServer(handleRequest);
www.listen(process.env.NODEPORT);
console.log("Listening at ", process.env.NODEPORT)
