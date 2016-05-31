import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.websocket
import tornado.httpclient
from tornado import gen
import os.path
import os
import json
import requests
import time
import datetime
from tornado.options import define, options, parse_command_line
define('port',default=8000,type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        response = {"version":"1.0.0",
        "data":"Data",
        }
        self.write(json.dumps(response))

class sendHandler(tornado.web.RequestHandler):
    def get(self):
        response = {"version":"1.0.0",
        "data":"Data",
        }
        self.write(json.dumps(response))
        
        
handlers = [
(r'/',IndexHandler),
(r'/send',SendHandler),

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

    print("Live at %s"%options.port)
    loop = tornado.ioloop.IOLoop.instance()
    loop.start()
