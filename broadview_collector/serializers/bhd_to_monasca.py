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

from broadviewserializerbase import BroadViewSerializerBase
from broadview_lib.bhd.bhd_parser import BHDParser, ReportTypes
import json
import unittest
import datetime
import time


class BHDToMonasca(BroadViewSerializerBase):
    '''
    Class that converts Black Hole Detection object model to OpenStack Monasca 
    metrics.
    See broadview-collector/doc/bhd_to_monasca_serializer.md for documentation
    '''

    def __init__(self):
        pass

    def __serializeToJSON(self, host, data):
        ret = []
        try:
            timestamp = time.mktime(data.getTimestamp()) * 1000
        except:
            timestamp = int(time.mktime(datetime.datetime.utcnow().timetuple())) \
                        * 1000 * 1000
        asic = data.getASICId()

        '''
        Note that monasca requires a value field. Where required, but not
        obvious value is present in the data, we use 0 and notate that the
        value is to be ignored in the metadata
        '''

        x = data.getBlackHoleEventReport()

        print("{}".format(x))
        m = {}
        m["name"] = "broadview.bhd." + repr(x)
        m["timestamp"] = timestamp
        m["dimensions"] = {}
        m["dimensions"]["asic-id"] = asic
        m["dimensions"]["bv-agent"] = host
        m["dimensions"]["ingress-port"] = x.getIngressPort()
        m["dimensions"]["egress-port-list"] = x.getEgressPortList()
        m["dimensions"]["sample-packet"] = x.getSamplePacket()
        m["dimensions"]["ignore-value"] = 0
        m["value"] = x.getBlackHoledPacketCount()
        ret.append(m)
            
        return json.dumps(ret)

    def serialize(self, host, data):
        # serialize a parsed BHD report to Monasca metrics
        ret = (False, None)

        s = self.__serializeToJSON(host, data)

        if s:
            ret = (True, s)

        return ret

    def __repr__(self):
        return "Black Hole Detection To Monasca Serializer" 

class TestSerializer(unittest.TestCase):

    def setUp(self):
        self._host = "127.0.0.1"
        self.black_hole_event_report_1 = {
   		"jsonrpc": "2.0",
   		"method": "get-black-hole-event-report",
   		"asic-id": "1",
   		"version": "2",
   		"time-stamp": "2014-11-18 - 00:15:04 ",
   		"report": {
       			"ingress-port": "1",
       			"egress-port-list": ["2",  "3"],
       			"black-holed-packet-count": 100,
       			"sample-packet": "0010203232.."
   		}
	}

    def test_black_hole_event_report_1(self):
        rep = BHDParser()
        rep.process(self.black_hole_event_report_1)
        serializer = BHDToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])

        dim = data[0]["dimensions"]

        self.assertTrue("bv-agent" in dim)
        self.assertTrue("asic-id" in dim)
        self.assertTrue("timestamp" in data[0])
        self.assertTrue("name" in data[0])
        self.assertEqual(data[0]["name"], "broadview.bhd.get-black-hole-event-report")
        self.assertTrue("dimensions" in data[0])
        timestamp = int(data[0]["timestamp"]) / 1000
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.black_hole_event_report_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        dim = data[0]["dimensions"]
        self.assertEqual(dim["asic-id"], self.black_hole_event_report_1["asic-id"])
        self.assertTrue("ingress-port" in dim)
        self.assertEqual(dim["ingress-port"], "1")
        self.assertTrue("egress-port-list" in dim)
        self.assertEqual(len(dim["egress-port-list"]), 2)
        self.assertTrue("2" in dim["egress-port-list"])
        self.assertTrue("3" in dim["egress-port-list"])
        self.assertTrue("sample-packet" in dim)
        self.assertEqual(dim["sample-packet"], "0010203232..")
        self.assertTrue("ignore-value" in dim)
        self.assertEqual(dim["ignore-value"], 0)
        self.assertTrue("value" in data[0])
        self.assertEqual(data[0]["value"], 100)

if __name__ == "__main__":
    unittest.main()

