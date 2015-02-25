#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.websocket
import tornado.options
import tornado.web
import tornado.escape
import uuid
import os
import redis
from marker import Marker
from tornado.options import define, options
from analyzer import Analyzer

define("port", default=8880, help="run on the given port", type=int)

DATASTORE_KEY = "15s_learning_data_"
G_Marker = Marker()
#store data
#G_Database = redis.Redis(host='localhost', port=6379, db=0)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class TextSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    Store_Number=101;
    Store_y=0;

    cache = []
    cache_size = 200

    def open(self):
        print("WebSocket opened\n")
        TextSocketHandler.waiters.add(self)

    def on_close(self):
        TextSocketHandler.waiters.remove(self)
        print ("Closed!!")

    def send_updates(self, message):
        logging.info("sending message to %r:%r", self, message)
        json_message = tornado.escape.json_encode(message)
        try:
            self.write_message(json_message)
        except:
            logging.error("Error sending message", exc_info=True)

    def on_message(self, messages):
        logging.info("got messages %r", messages)
        received = tornado.escape.json_decode(messages)
        analyzer = Analyzer()

        # print(parsed)
        analyze_result = analyzer.analyze(received)
        for k in analyze_result:
            received[k] = analyze_result[k]

        if G_Marker.model1 is None:
            G_Marker.load()

        received["score"],received["score2"] = G_Marker.cal_score(analyze_result)
        print(received["score"])
        print(received["score2"])
        #store data
        #if received["status"]!=True:
        #    self.store_message(received)
        self.send_updates(received)

    def store_message(self, message):
        store_name=DATASTORE_KEY+str(self.Store_Number)
        store={}
        store_keys=["message","interval","sentenceCount","speed","sentenceSpeed","parts","parts_speed","characters"]
        print("保存しました")
        for keys in store_keys:
            store[keys]=message[keys]
        store["y"]=self.Store_y
        G_Database.rpush(store_name,store)
        self.Store_Number+=1


def main():
    io=tornado.ioloop.IOLoop.instance()
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", TextSocketHandler)
        ],
        template_path=os.path.join(os.getcwd(),  "templates"),
        static_path=os.path.join(os.getcwd(),  "static"),
        debug=True,
    )
    if os.path.isdir(os.path.join(os.path.dirname(__file__), "ssl")):
        http_server = tornado.httpserver.HTTPServer(application, ssl_options={
        "keyfile": os.path.join(os.path.dirname(__file__), "ssl/serverkey.pem"),
        "certfile": os.path.join(os.path.dirname(__file__), "ssl/servercrt.pem"),
    })
    else:
        http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 8880))
    http_server.listen(port)
    io.start()


if __name__ == "__main__":
    main()