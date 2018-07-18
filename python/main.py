from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import os
# HTTPRequestHandler class


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        res_value = ""
        try:
            server = "http://" + os.environ["NODE_SERVER"]
            print(server)
            res_value = requests.get(server).text
        except:
            print("Something went wrong connecting to the node server")

        # Send message back to client
        if (len(res_value)):
            message = "Node Server is now talking to Python"
        else:
            message = "There was no response"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print('starting server...')
    try:
        print("Node server at:" + os.environ['NODE_SERVER'])
    except:
        print("No NODE_SERVER defined")
    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    print("Listening at port: ", os.environ['PYPORT'])
    server_address = ('0.0.0.0', int(os.environ['PYPORT']))
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()
