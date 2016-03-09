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

# the Monasca serializer format is suitable for logging output,
# so use it. 

from broadview_collector.serializers.bst_to_monasca import BSTToMonasca
import json
from oslo_log import log
import ConfigParser

LOG = log.getLogger(__name__)

class BroadViewPublisher(BroadViewPublisherBase):
    def readConfig(self):
        try:
            cfg = ConfigParser.ConfigParser()
            cfg.read("/etc/broadviewcollector.conf")
            self._logfile = cfg.get("logging", "file")
        except:
            LOG.info("log publisher: unable to process log file")

        try:
            self._f = open(self._logfile, "w+")
        except:
            LOG.info("log publisher: unable to open log file {}".format(self.__logfile))

    def __init__(self):
        LOG.info("log publisher: init")
        self._f = None
        self._logfile = "/tmp/broadview-bstlogging.log"
        self.readConfig()

    def __del__(self):
        if self._f:
            self._f.close()

    def publish(self, data):
        LOG.info("log publisher: publish")
        code = 200
        success, sdata = BSTToMonasca().serialize(data)
        sdata = json.loads(sdata)
        if success: 
            for x in sdata:
                print >>self._f, json.dumps(x)
            self._f.flush()
        else:
            code = 500
        return code

    def __repr__(self):
        return "BroadView Log Publisher"

