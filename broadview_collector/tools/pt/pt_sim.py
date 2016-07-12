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

import json
import requests
import datetime
import time

'''
Base class for packet trace agent simulation classes

'''

class PTSim(object):

    def __init__(self, host=None, port=None):
        if not host:
            self._host = "127.0.0.1"
        else:
            self._host = host
        if not port:
            self._port = 8082
        else:
            self._port = port
        self.setUp()

    def setUp(self):
        # convert datetime string to timestamp

        d = str(datetime.datetime.now()).split(" ")
        t = d[1].split(".")[0]
        self._timestamp = "{} - {}".format(d[0], t)

        # initialize data, overridden by subclass
        self._data = None

    def send(self):
        j = json.dumps(self._data)
        r = requests.post('http://{}:{}'.format(self._host, self._port), json=j)

