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
from monascaclient import client
import monascaclient.exc as exc
from broadview_collector.serializers.bst_to_monasca import BSTToMonasca
from broadview_collector.serializers.pt_to_monasca import PTToMonasca
import json
import ConfigParser

try:
    from oslo_log import log 
except:
    import logging as log 

LOG = log.getLogger(__name__)

class BroadViewPublisher(BroadViewPublisherBase):

    def readConfig(self):
        try:
            bvcfg = ConfigParser.ConfigParser()
            bvcfg.read("/etc/broadviewcollector.conf")
            self._endpoint = bvcfg.get("monasca", "endpoint")
            self._username = bvcfg.get("monasca", "username") 
            self._password = bvcfg.get("monasca", "password") 
            self._project_name = bvcfg.get("monasca", "project_name") 
            self._auth_url = bvcfg.get("monasca", "auth_url") 
            self._endpoint = bvcfg.get("monasca", "endpoint") 
            self._api_version = bvcfg.get("monasca", "api_version") 
        except:
            LOG.error("BroadViewPublisher: unable to read configuration")

    def __init__(self):

        self.readConfig()
        try:
            self._auth_kwargs = {
                'username': self._username,
                'password': self._password,
                'auth_url': self._auth_url,
                'project_name': self._project_name,
            }


            self._monasca_client = client.Client(self._api_version, \
                                                 self._endpoint, \
                                                 **self._auth_kwargs)
        except:
            LOG.error("BroadViewPublisher: failed to parse config")
            self._monasca_client = None

    def publish(self, host, data):
        code = 500
        if self._monasca_client:
            if self.isBST(data):
                success, sdata = BSTToMonasca().serialize(host, data)
            elif self.isPT(data):
                success, sdata = PTToMonasca().serialize(host, data)
            else:
                success = False
                sdata = None
            if success: 
                code = 200
                sdata = json.loads(sdata)
                for x in sdata:
                    try:
                        resp = self._monasca_client.metrics.create(**x)
                        if not resp.status_code == 200 and not resp.status_code == 204:
                            code = resp.status_code
                            break
                    except exc.HTTPException as he:
                        LOG.error('HTTPException code=%s message=%s' % (he.code, he.message))
                        code = he.code
                        break
        return code

    def __repr__(self):
        return "BroadView Monasca Publisher {}".format(self.__dict__) 

