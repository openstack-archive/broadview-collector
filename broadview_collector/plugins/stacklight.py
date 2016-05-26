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

from broadviewpublisherbase import BroadViewPublisherBase
from broadview_collector.serializers.bst_to_stacklight import BSTToStacklight
import json
import ConfigParser
import requests

try:
    from oslo_log import log 
except:
    import logging as log 

LOG = log.getLogger(__name__)

class BroadViewPublisher(BroadViewPublisherBase):

    def readConfig(self):
        self._ipaddr = "127.0.0.1"
        self._port = 8088
        self._timeout = 0.5
        try:
            bvcfg = ConfigParser.ConfigParser()
            bvcfg.read("/etc/broadviewcollector.conf")
            try:
                self._ipaddr = bvcfg.get("stacklight", "ip_address")
            except:
                LOG.info("BroadViewPublisher: unable to read stacklight ip_address")
            try:
                self._port = bvcfg.get("stacklight", "port") 
            except:
                LOG.info("BroadViewPublisher: unable to read stacklight port")
            try:
                self._timeout = bvcfg.get("stacklight", "timeout") 
            except:
                LOG.info("BroadViewPublisher: unable to read stacklight timeout")
        except:
            LOG.error("BroadViewPublisher: unable to read stacklight configuration")

    def __init__(self):
        self.readConfig()

    def publish(self, host, data):
        code = 500
        success, sdata = BSTToStacklight().serialize(host, data)
        if success: 
            sdata = json.loads(sdata)
	    for x in sdata:
                try:
                    r = requests.post('http://{}:{}'.format(self._ipaddr, self._port), json=sdata, timeout=self._timeout)
                    code = r.status_code
                except requests.exceptions.Timeout:
                    LOG.error('BroadViewPublisher timeout {} seconds {}:{}'.format(self._timeout, self._ipaddr, self._port))
                    code = 500
                    break
                except requests.exceptions.RequestException as e:
                    LOG.error('BroadViewPublisher {} {}:{}'.format(e, self._ipaddr, self._port))
                    code = 500
                    break
                if r.status_code != 200:
                    LOG.error('BroadViewPublisher received {}'.format(r.status_code))
                    break
        return code

    def __repr__(self):
        return "BroadView Stacklight Publisher" 
