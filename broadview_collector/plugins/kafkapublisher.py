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
from kafka import KafkaProducer
from broadview_collector.serializers.bst_to_monasca import BSTToMonasca
import json
import ConfigParser

from oslo_log import log 

LOG = log.getLogger(__name__)

class BroadViewPublisher(BroadViewPublisherBase):
    def readConfig(self):
        try:
            bvcfg = ConfigParser.ConfigParser()
            bvcfg.read("/etc/broadviewcollector.conf")
            self._ip_address = bvcfg.get("kafka", "ip_address")
            self._port = bvcfg.get("kafka", "port") 
            self._topic = bvcfg.get("kafka", "topic") 
        except:
            LOG.info("BroadViewPublisher: unable to read configuration")

    def getKafkaProducer(self):
        try:
	    self._producer = KafkaProducer(bootstrap_servers=['{}:{}'.format(self._ip_address, self._port)])
        except kafka.errors.NoBrokersAvailable as e:
            LOG.error("BroadViewPublisher: NoBrokersAvailable {}".format(e))
        except:
            LOG.error("Unexpected error: {}".format(sys.exc_info()[0]))

    def __init__(self):
	self._ip_address = "127.0.0.1"
	self._port = "9092"
	self._topic = "broadview-bst"
        self.readConfig()
        self._producer = None

    def publish(self, host, data):
        LOG.info('kafka publish enter')
        code = 500
        #  get a producer if needed
        if not self._producer:
            self.getKafkaProducer()
        if self._producer: 
	    code = 200
            success, sdata = BSTToMonasca().serialize(host, data)
	    sdata = json.loads(sdata)
            if success: 
	        for x in sdata:
                    try:
			self._producer.send(self._topic, json.dumps(x))
                    except:
                        LOG.info('unable to send to kafka topic {}: {}'.format(self._topic, sys.exc_info()[0]))
            else:
                code = 500
        LOG.info('kafka publish code {}'.format(code))
        return code

    def __repr__(self):
        return "BroadView kafka Publisher {} {}:{}".format(self._topic, self._ip_address, self._port) 

