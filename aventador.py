#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-08-23
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os, logging
from modules.AvenUOM import AvenUOM

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

def load_actions():
    AvenUOM.import_module("actions.todo")

def start():
    """启动"""
    tornado.options.parse_command_line()
    load_actions()
    handlers = AvenUOM.load()
    logging.info("application.handlers: %s" % str(handlers))
    app = tornado.web.Application(
        handlers=handlers,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    start()
