from tornado import gen
from gcm import GCM
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.websocket
import tornado.httpclient
import os.path
import os
import json
import requests
import time
import datetime
import subprocess

from tornado.options import define, options, parse_command_line
define('port',default=8000,type=int)

#apiKey that we got from the Google Developer console
apiKey = "AIzaSyBfI5t4-GW5VovfzQ6BpvhTd2dkUB7L9R0"
subprocess.Popen(["node","push_ios_android_server.js"])

def pushNotification(plat, deviceID):
    if plat=="Android":
        gcm = GCM(apiKey, debug=True)
        data = {"title":"any notification string",
                "body":"This is the body"}
        response = gcm.plaintext_request(registration_id=deviceID, data=data)
        
        
    if plat=="iOS":
        messageToSend = {"devicePlatform":plat,"deviceId":deviceID}
        a = requests.post("http://192.168.1.89:8080/receivetoken",json=messageToSend)
        # TODO: send the deviceID through API to APNS node server


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        response = {"version":"1.0.0", "data":"Data", }
        self.write(json.dumps(response))


class PushHandler(tornado.web.RequestHandler):
    def post(self):
        requestReceived = json.loads((self.request.body).decode('utf-8'))
        platform = requestReceived["platform"]
        deviceID = requestReceived["deviceID"]
        pushNotification(platform, deviceID)
        response = {"status" : "OK"}
        self.write(json.dumps(response))
        
        
handlers = [
	(r'/',IndexHandler),
	(r'/push',PushHandler),
]


if __name__ == "__main__":
    parse_command_line()
    # template path should be given here only unlike handlers
    app = tornado.web.Application(handlers, template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"), cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=", debug=True)
    http_server = tornado.httpserver.HTTPServer(app)

    master_file = open("push.pid", "w")
    master_file.write("push.pid is: %s"%os.getpid())
    master_file.close()
    http_server.listen(options.port)

    print("Server Live at %s"%options.port)
    loop = tornado.ioloop.IOLoop.instance()
    loop.start()
