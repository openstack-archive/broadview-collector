#!/usr/bin/env python

# (C) Copyright Broadcom Corporation 2016
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import threading
import argparse
import re
import cgi
import datetime
import json
from time import sleep
import ConfigParser
import os
import sys
from importlib import import_module
import ast
from oslo_log import log as logging
from oslo_config import cfg

LOG = logging.getLogger(__name__)

class BroadViewCollector(object):
    def __init__(self):
        logging.register_options(cfg.CONF)
        logging.set_defaults()
        cfg.CONF(args=[],
                project="broadview_collector",
                default_config_files=["/etc/broadviewcollector.conf"])
        logging.setup(cfg.CONF, 'broadview_collector')
        self._publishers = [] 
        self._handlers = [] 

    def readConfig(self):
        LOG.info("broadview_collector: readConfig")
        try:
            cfg = ConfigParser.ConfigParser()
            cfg.read("/etc/broadviewcollector.conf")
            x = cfg.get("plugins", "publishers")
            self._publisherNames = [y.strip() for y in x.split(',')]
            LOG.info("publishers {}".format(self._publisherNames))
            self._searchpath = []
            try:
                x = cfg.get("plugins", "searchpath")
                self._searchpath = [y.strip() for y in x.split(',')]
            except:
                LOG.info("plugin searchpath missing or malformed")

            if not self._searchpath or len(self._searchpath) == 0:
                self._searchpath = ["broadview_collector.plugins"]
            else:
                self._searchpath.append("broadview_collector.plugins")
            LOG.info("plugin searchpath {}".format(self._searchpath))

            x = cfg.get("plugins", "handlers")
            self._handlerNames = [y.strip() for y in x.split(',')]
            LOG.info("plugin handlers {}".format(self._handlerNames))
            self._ip_address = cfg.get("network", "ip_address")
            self._port = int(cfg.get("network", "port"))

        except:
            LOG.error("Unable to open or read /etc/broadviewcollector.conf")
            exit()

    def loadPublishers(self):
        LOG.info("broadview_collector: loadPublishers")
        self._publishers = []
        for x in self._publisherNames: 
            for y in self._searchpath:
                try:
                    path = "{}.{}".format(y, x)
                    mod = import_module(path)
                    classattr = getattr(mod, "BroadViewPublisher")
                    self._publishers.append(classattr())
                    LOG.info("loaded plugin %s" % (path))
                    break
                except:
                    e = sys.exc_info()[0]
                    LOG.info("Unable to load plugin %s: %s" % (path, e))

    def loadHandlers(self):
        LOG.info("broadview_collector: loadHandlers")
        self._handlers = []
        for x in self._handlerNames: 
            try:
                mod = import_module("broadview_collector.handlers." + x)
                classattr = getattr(mod, "BroadViewHandler")
                self._handlers.append(classattr())
                LOG.info("imported handler %s" % ("broadview_collector.handlers." + x))
            except:
                e = sys.exc_info()[0]
                LOG.info("Unable to load handler %s: %s" % (x, e))
                exit()

    def handlePOST(self, path, ctype, length, data):
        '''
        find a handler that can handle the request, and then if
        successful, send it to all publishers
        '''

        handled = False
        retcode = 404
        LOG.info("broadview_collector: handlePOST")

        for x in self._handlers:
            o, handled = x.handlePOST(path, ctype, length, data)
            if handled: 
                for y in self._publishers:
                    code = y.publish(o)
		    if not code == 200:
                        LOG.info("handlePOST: {} failed to publish, code: {}".format(y, code))
                retcode = 200
                break
        LOG.info("broadview_collector: handlePOST returns %d" % (retcode))
        return retcode

collector = BroadViewCollector()

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        pass

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        length = int(self.headers.getheader('content-length'))
        data = ast.literal_eval(json.loads(self.rfile.read(length)))
        code = collector.handlePOST(self.path, ctype, length, data)
        data = json.dumps({})
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(data)

        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
 
    def shutdown(self):
        self.socket.close()
        HTTPServer.shutdown(self)
 
class SimpleHttpServer():
    def __init__(self, ip, port):
        self.server = ThreadedHTTPServer((ip,port), HTTPRequestHandler)
 
    def start(self):
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
 
    def waitForThread(self):
        self.server_thread.join()
 
    def stop(self):
        self.server.shutdown()
        self.waitForThread()

def main():
    collector.readConfig()
    collector.loadPublishers()
    collector.loadHandlers()
    server = SimpleHttpServer(collector._ip_address, collector._port)
    LOG.info('HTTP Server Running...........')
    server.start()
    server.waitForThread()
 
if __name__=='__main__':
    main()
