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
from broadview_lib.pt.pt_parser import PTParser, ReportTypes
import json
import unittest
import datetime
import time


class PTToMonasca(BroadViewSerializerBase):
    '''
    Class that converts Packet Trace object model to OpenStack Monasca metrics.
    See broadview-collector/doc/pt_to_monasca_serializer.md for documentation
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

        d = data.getPacketTraceProfile()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.pt." + repr(x)
                m["timestamp"] = timestamp
                m["value"] = 0
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["realm"] = y.getRealm()
                m["dimensions"]["port"] = y.getPort()
                r = y.getLAGLinkResolution()
                if r:
                    m["dimensions"]["lag-id"] = r.getLAGID()
                    m["dimensions"]["dst-lag-member"] = r.getDstLAGMember()
                    m["dimensions"]["lag-members"] = r.getLAGMembers()
                    m["dimensions"]["fabric-trunk-members"] = r.getFabricTrunkMembers()
                    m["dimensions"]["fabric-trunk-id"] = r.getFabricTrunkID()
                    m["dimensions"]["ignore-value"] = 1
                    ret.append(m)
                else:
                    r = y.getECMPLinkResolution()
                    for l in r:
                        m = {}
                        m["name"] = "broadview.pt." + repr(x)
                        m["timestamp"] = timestamp
                        m["value"] = 0
                        m["dimensions"] = {}
                        m["dimensions"]["ignore-value"] = 1
                        m["dimensions"]["asic-id"] = asic
                        m["dimensions"]["bv-agent"] = host
                        m["dimensions"]["realm"] = y.getRealm()
                        m["dimensions"]["port"] = y.getPort()
                        m["dimensions"]["ecmp-group-id"] = l.getECMPGroupID()
                        m["dimensions"]["ecmp-dst-member"] = l.getECMPDstMember()
                        m["dimensions"]["ecmp-dst-port"] = l.getECMPDstPort()
                        m["dimensions"]["ecmp-next-hop-ip"] = l.getECMPNextHopIP()
                        m["dimensions"]["ecmp-members"] = []
                        for mem in l.getECMPMembers():
                            member = {}
                            member["id"] = mem.getId()
                            member["ip"] = mem.getIP()
                            member["port"] = mem.getPort()
                            m["dimensions"]["ecmp-members"].append(member)
                        ret.append(m)

        d = data.getPacketTraceECMPResolution()
        for x in d:
            r = x.getECMPLinkResolution()
            for l in r:
                m = {}
                m["name"] = "broadview.pt." + repr(x)
                m["timestamp"] = timestamp
                m["value"] = 0
                m["dimensions"] = {}
                m["dimensions"]["ignore-value"] = 1
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = x.getPort()
                m["dimensions"]["ecmp-group-id"] = l.getECMPGroupID()
                m["dimensions"]["ecmp-dst-member"] = l.getECMPDstMember()
                m["dimensions"]["ecmp-dst-port"] = l.getECMPDstPort()
                m["dimensions"]["ecmp-next-hop-ip"] = l.getECMPNextHopIP()
                m["dimensions"]["ecmp-members"] = []
                for mem in l.getECMPMembers():
                    member = {}
                    member["id"] = mem.getId()
                    member["ip"] = mem.getIP()
                    member["port"] = mem.getPort()
                    m["dimensions"]["ecmp-members"].append(member)
                ret.append(m)
            
        d = data.getPacketTraceLAGResolution()
        for x in d:
            ll = x.getLAGLinkResolution()
            m = {}
            m["name"] = "broadview.pt." + repr(x)
            m["timestamp"] = timestamp
            m["dimensions"] = {}
            m["dimensions"]["asic-id"] = asic
            m["dimensions"]["bv-agent"] = host
            m["dimensions"]["port"] = x.getPort()
            m["dimensions"]["lag-id"] = ll.getLAGID()
            m["dimensions"]["dst-lag-member"] = ll.getDstLAGMember()
            m["dimensions"]["lag-members"] = ll.getLAGMembers()
            m["dimensions"]["fabric-trunk-members"] = ll.getFabricTrunkMembers()
            m["dimensions"]["fabric-trunk-id"] = ll.getFabricTrunkID()
            m["dimensions"]["ignore-value"] = 1
            m["value"] = 0
            ret.append(m)
            
        d = data.getPacketTraceDropReason()
        for x in d:
            m = {}
            m["name"] = "broadview.pt." + repr(x)
            m["timestamp"] = timestamp
            m["dimensions"] = {}
            m["dimensions"]["asic-id"] = asic
            m["dimensions"]["bv-agent"] = host
            m["dimensions"]["reason"] = x.getReason()
            m["dimensions"]["port-list"] = x.getPortList()
            m["dimensions"]["send-dropped-packet"] = x.getSendDroppedPacket()
            m["dimensions"]["trace-profile"] = x.getTraceProfile()
            m["dimensions"]["packet-threshold"] = x.getPacketThreshold()
            m["dimensions"]["ignore-value"] = 0
            m["value"] = x.getPacketCount()
            ret.append(m)
            
        d = data.getPacketTraceDropCounterReport()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.pt." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["realm"] = y.getRealm()
                m["dimensions"]["port"] = y.getPort()
                m["value"] = y.getCount()
                m["dimensions"]["ignore-value"] = 0
                ret.append(m)

        d = data.getPacketTraceSupportedDropReasons()
        if d:
            m = {}
            m["name"] = "broadview.pt." + repr(d)
            m["timestamp"] = timestamp
            m["dimensions"] = {}
            m["dimensions"]["asic-id"] = asic
            m["dimensions"]["bv-agent"] = host
            m["dimensions"]["reasons"] = d.getReasons()
            m["dimensions"]["ignore-value"] = 1
            m["value"] = 0
            ret.append(m)

        return json.dumps(ret)

    def serialize(self, host, data):
        # serialize a parsed BST report to Monasca metrics
        ret = (False, None)

        s = self.__serializeToJSON(host, data)

        if s:
            ret = (True, s)

        return ret

    def __repr__(self):
        return "Packet Trace To Monasca Serializer" 

class TestSerializer(unittest.TestCase):

    def setUp(self):
        self._host = "127.0.0.1"
        self.packet_trace_profile_1 = {
            "jsonrpc": "2.0",
            "method": "get-packet-trace-profile",
            "asic-id": "1",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "port": "1",
                    "trace-profile": [
                        {
                            "realm": "lag-link-resolution",
                            "data": {
                                "lag-id": "2",
                                "lag-members": ["1", "2", "3", "4"],
                                "dst-lag-member": "4",
                                "fabric-trunk-id": "6",
                                "fabric-trunk-members": ["27", "28", "29"],
                            }
                        },
                        {
                            "realm": "ecmp-link-resolution",
                            "data": 
                            [
                                {
                                    "ecmp-group-id": "100256",
                                    "ecmp-members": [["100004", "1.2.2.2", "18"],["100005", "1.6.6.1", "11"]],
                                    "ecmp-dst-member": "100005",
                                    "ecmp-dst-port": "11",
                                    "ecmp-next-hop-ip": "1.6.6.2"
                                },
                                {
                                    "ecmp-group-id": "200100",
                                    "ecmp-members": [["200001", "2.3.3.1", "21"], ["200002", "2.7.7.2", "21"]],
                                    "ecmp-dst-member": "200001",
                                    "ecmp-dst-port": "21",
                                    "ecmp-next-hop-ip": "2.3.3.2"
                                }
                            ]
                        }
                    ]
                },
                {
                    "port": "2",
                    "trace-profile": [
                        {
                            "realm": "lag-link-resolution",
                            "data": {
                                "lag-id": "2",
                                "lag-members": ["5", "6", "7", "8"],
                                "dst-lag-member": "5",
                                "fabric-trunk-id": "7",
                                "fabric-trunk-members": ["37", "38", "39"],
                            }
                        },
                        {
                            "realm": "ecmp-link-resolution",
                            "data": 
                            [
                                {
                                    "ecmp-group-id": "300256",
                                    "ecmp-members": [["300004", "3.2.2.2", "38"],["300005", "3.6.6.1", "31"]],
                                    "ecmp-dst-member": "300005",
                                    "ecmp-dst-port": "31",
                                    "ecmp-next-hop-ip": "3.6.6.2"
                                },
                                {
                                    "ecmp-group-id": "400100",
                                    "ecmp-members": [["400001", "4.3.3.1", "48"], ["400002", "4.7.7.2", "41"]],
                                    "ecmp-dst-member": "400001",
                                    "ecmp-dst-port": "41",
                                    "ecmp-next-hop-ip": "4.3.3.2"
                                }
                            ]
                        }
                    ]
                } 
            ],
            "id": 1
        }
        self.packet_trace_lag_resolution_1 = {
            "jsonrpc": "2.0",
            "method": " get-packet-trace-lag-resolution",
            "asic-id": "1",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "port": "1",
                    "lag-link-resolution": {
                        "lag-id": "1",
                        "lag-members": [
                            "1",
                            "2",
                            "3",
                            "4"
                        ],
                        "dst-lag-member": "4",
                        "fabric-trunk-id": "8",
                        "fabric-trunk-members": ["47", "48", "49"],
                    }
                },
                {
                    "port": "2",
                    "lag-link-resolution": {
                        "lag-id": "2",
                        "lag-members": [
                            "5",
                            "6",
                            "7",
                            "8"
                        ],
                        "dst-lag-member": "7",
                        "fabric-trunk-id": "9",
                        "fabric-trunk-members": ["57", "58", "59"],
                    }
                }
            ],
            "id": 1
        }

        self.packet_trace_ecmp_resolution_1 = {
            "jsonrpc": "2.0",
            "method": " get-packet-trace-ecmp-resolution",
            "asic-id": "1",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "port": "1",
                    "ecmp-link-resolution": [
                        {
                            "ecmp-group-id": "100256",
                            "ecmp-members": [["100004", "1.2.2.2", "18"],["100005", "1.6.6.1", "11"]],
                            "ecmp-dst-member": "100005",
                            "ecmp-dst-port": "11",
                            "ecmp-next-hop-ip": "1.6.6.2"
                        },
                        {
                            "ecmp-group-id": "200100",
                            "ecmp-members": [["200001", "2.3.3.1", "21"], ["200002", "2.7.7.2", "21"]],
                            "ecmp-dst-member": "200001",
                            "ecmp-dst-port": "21",
                            "ecmp-next-hop-ip": "2.3.3.2"
                        }
                    ]
                },
                {
                    "port": "2",
                    "ecmp-link-resolution": [
                        {
                            "ecmp-group-id": "300100",
                            "ecmp-members": [["300001", "3.3.3.1", "38"],["300002", "3.7.7.2", "31"]],
                            "ecmp-dst-member": "300005",
                            "ecmp-dst-port": "31",
                            "ecmp-next-hop-ip": "3.6.6.2"
                        },
                        {
                            "ecmp-group-id": "400100",
                            "ecmp-members": [["400001", "4.3.3.1", "48"], ["400002", "4.7.7.2", "41"]],
                            "ecmp-dst-member": "400001",
                            "ecmp-dst-port": "41",
                            "ecmp-next-hop-ip": "4.3.3.2"
                        }
                    ]
                }
            ],
            "id": 1
        }

        self.packet_trace_drop_reason_1 = {
            "jsonrpc": "2.0",
            "method": "get-packet-trace-drop-reason",
            "asic-id": "1",
            "version": "1",
            "result": [
                {
                    "reason": "l2-lookup-failure",
                    "port-list": [
                        "1",
                        "5",
                        "6",
                        "10-15"
                    ],
                    "send-dropped-packet": 0,
                    "trace-profile": 0,
                    "packet-count": 4,
                    "packet-threshold": 0
                },
                {
                    "reason": "vlan-mismatch",
                    "port-list": [
                        "11",
                        "15",
                        "16",
                        "20-25"
                    ],
                    "send-dropped-packet": 1,
                    "trace-profile": 1,
                    "packet-count": 3,
                    "packet-threshold": 10
                }
            ],
            "id": 1
        }

        self.packet_trace_drop_counter_report_1 = {
            "jsonrpc": "2.0",
            "method": " get-packet-trace-drop-counter-report",
            "asic-id": "1",
            "version": "1",
            "report": [
                {
                    "realm": "vlan-xlate-miss-drop",
                    "data": [
                        {
                            "port": "1",
                            "count": 10
                        },
                        {
                            "port": "5",
                            "count": 20
                        },
                        {
                            "port": "6",
                            "count": 30
                        },
                        {
                            "port": "10",
                            "count": 40
                        },
                        {
                            "port": "11",
                            "count": 50
                        },
                        {
                            "port": "12",
                            "count": 60
                        }
                    ]
                },
                {
                    "realm": "bpdu-drop",
                    "data": [
                        {
                            "port": "1",
                            "count": 70
                        },
                        {
                            "port": "5",
                            "count": 20
                        },
                        {
                            "port": "6",
                            "count": 30
                        },
                        {
                            "port": "10",
                            "count": 40
                        },
                        {
                            "port": "11",
                            "count": 80
                        },
                        {
                            "port": "12",
                            "count": 90
                        }
                    ]
                },
                {
                    "realm": "trill-slowpath-drop",
                    "data": [
                        {
                            "port": "1",
                            "count": 10
                        },
                        {
                            "port": "5",
                            "count": 20
                        },
                        {
                            "port": "6",
                            "count": 30
                        },
                        {
                            "port": "10",
                            "count": 40
                        },
                        {
                            "port": "11",
                            "count": 50
                        },
                        {
                            "port": "12",
                            "count": 60
                        }
                    ]
                }
            ]
        }

        self.packet_trace_supported_drop_reasons_1 = {
            "jsonrpc": "2.0",
            "method": "get-packet-trace-supported-drop-reasons",
            "asic-id": "1",
            "version": "1",
            "result": [
                "l2-lookup-failure",
                "vlan-mismatch"
            ],
            "id": 1
        }

    def test_packet_trace_profile_1(self):
        rep = PTParser()
        rep.process(self.packet_trace_profile_1)
        serializer = PTToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)

        self.assertTrue("timestamp" in data[0])
        timestamp = int(data[0]["timestamp"]) / 1000
        self.assertTrue("name" in data[0])
        self.assertTrue("dimensions" in data[0])
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.packet_trace_profile_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data[0]["name"], "broadview.pt.packet-trace-profile")
        dim = data[0]["dimensions"]
        self.assertTrue("bv-agent" in dim)
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.packet_trace_profile_1["asic-id"])
        self.assertTrue("realm" in dim)
        self.assertEqual(dim["realm"], "lag-link-resolution")
        self.assertTrue("lag-id" in dim)
        self.assertEqual(dim["lag-id"], "2")
        self.assertTrue("lag-members" in dim)
        self.assertEqual(len(dim["lag-members"]), 4)
        self.assertTrue("1" in dim["lag-members"])
        self.assertTrue("2" in dim["lag-members"])
        self.assertTrue("3" in dim["lag-members"])
        self.assertTrue("4" in dim["lag-members"])
        self.assertTrue("port" in dim)
        self.assertEqual(dim["port"], "1")
        self.assertTrue("dst-lag-member" in dim)
        self.assertEqual(dim["dst-lag-member"], "4")
        self.assertTrue("fabric-trunk-id" in dim)
        self.assertEqual(dim["fabric-trunk-id"], "6")
        self.assertTrue("fabric-trunk-members" in dim)
        self.assertEqual(len(dim["fabric-trunk-members"]), 3)
        self.assertTrue("27" in dim["fabric-trunk-members"])
        self.assertTrue("28" in dim["fabric-trunk-members"])
        self.assertTrue("29" in dim["fabric-trunk-members"])

        self.assertTrue("timestamp" in data[1])
        timestamp = int(data[1]["timestamp"]) / 1000
        self.assertTrue("name" in data[1])
        self.assertTrue("dimensions" in data[1])
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.packet_trace_profile_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data[1]["name"], "broadview.pt.packet-trace-profile")
        dim = data[1]["dimensions"]
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.packet_trace_profile_1["asic-id"])
        self.assertTrue("realm" in dim)
        self.assertEqual(dim["realm"], "ecmp-link-resolution")
        self.assertTrue("ecmp-dst-member" in dim)
        self.assertEqual(dim["ecmp-dst-member"], "100005")
        self.assertTrue("bv-agent" in dim)
        self.assertTrue("ecmp-next-hop-ip" in dim)
        self.assertEqual(dim["ecmp-next-hop-ip"], "1.6.6.2")
        self.assertTrue("ecmp-dst-port" in dim)
        self.assertEqual(dim["ecmp-dst-port"], "11")
        self.assertTrue("ecmp-members" in dim)
        self.assertEqual(len(dim["ecmp-members"]), 2)
        mem = dim["ecmp-members"][0]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "1.2.2.2")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "100004")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "18")
        mem = dim["ecmp-members"][1]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "1.6.6.1")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "100005")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "11")
        self.assertTrue("ecmp-group-id" in dim)
        self.assertEqual(dim["ecmp-group-id"], "100256")
        self.assertTrue("port" in dim)
        self.assertEqual(dim["port"], "1")

        self.assertTrue("timestamp" in data[2])
        timestamp = int(data[1]["timestamp"]) / 1000
        self.assertTrue("name" in data[2])
        self.assertTrue("dimensions" in data[2])
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.packet_trace_profile_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data[2]["name"], "broadview.pt.packet-trace-profile")
        dim = data[2]["dimensions"]
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.packet_trace_profile_1["asic-id"])
        self.assertTrue("realm" in dim)
        self.assertEqual(dim["realm"], "ecmp-link-resolution")
        self.assertTrue("ecmp-dst-member" in dim)
        self.assertEqual(dim["ecmp-dst-member"], "200001")
        self.assertTrue("bv-agent" in dim)
        self.assertTrue("ecmp-next-hop-ip" in dim)
        self.assertEqual(dim["ecmp-next-hop-ip"], "2.3.3.2")
        self.assertTrue("ecmp-dst-port" in dim)
        self.assertEqual(dim["ecmp-dst-port"], "21")
        self.assertTrue("ecmp-members" in dim)
        self.assertEqual(len(dim["ecmp-members"]), 2)
        mem = dim["ecmp-members"][0]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "2.3.3.1")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "200001")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "21")
        mem = dim["ecmp-members"][1]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "2.7.7.2")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "200002")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "21")
        self.assertTrue("ecmp-group-id" in dim)
        self.assertEqual(dim["ecmp-group-id"], "200100")
        self.assertTrue("port" in dim)
        self.assertEqual(dim["port"], "1")

    def test_packet_trace_lag_resolution_1(self):
        rep = PTParser()
        rep.process(self.packet_trace_lag_resolution_1)
        serializer = PTToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)

        self.assertTrue("timestamp" in data[0])
        timestamp = int(data[0]["timestamp"]) / 1000
        self.assertTrue("name" in data[0])
        self.assertTrue("dimensions" in data[0])
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.packet_trace_lag_resolution_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data[0]["name"], "broadview.pt.packet-trace-lag-resolution")
        dim = data[0]["dimensions"]
        self.assertTrue("bv-agent" in dim)
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.packet_trace_profile_1["asic-id"])
        self.assertTrue("lag-id" in dim)
        self.assertEqual(dim["lag-id"], "1")
        self.assertTrue("lag-members" in dim)
        self.assertEqual(len(dim["lag-members"]), 4)
        self.assertTrue("1" in dim["lag-members"])
        self.assertTrue("2" in dim["lag-members"])
        self.assertTrue("3" in dim["lag-members"])
        self.assertTrue("4" in dim["lag-members"])
        self.assertTrue("port" in dim)
        self.assertEqual(dim["port"], "1")
        self.assertTrue("dst-lag-member" in dim)
        self.assertEqual(dim["dst-lag-member"], "4")
        self.assertTrue("fabric-trunk-id" in dim)
        self.assertEqual(dim["fabric-trunk-id"], "8")
        self.assertTrue("fabric-trunk-members" in dim)
        self.assertEqual(len(dim["fabric-trunk-members"]), 3)
        self.assertTrue("47" in dim["fabric-trunk-members"])
        self.assertTrue("48" in dim["fabric-trunk-members"])
        self.assertTrue("49" in dim["fabric-trunk-members"])

        self.assertTrue("timestamp" in data[1])
        timestamp = int(data[0]["timestamp"]) / 1000
        self.assertTrue("name" in data[1])
        self.assertTrue("dimensions" in data[1])
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.packet_trace_lag_resolution_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data[1]["name"], "broadview.pt.packet-trace-lag-resolution")
        dim = data[1]["dimensions"]
        self.assertTrue("bv-agent" in dim)
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.packet_trace_profile_1["asic-id"])
        self.assertTrue("lag-id" in dim)
        self.assertEqual(dim["lag-id"], "2")
        self.assertTrue("lag-members" in dim)
        self.assertEqual(len(dim["lag-members"]), 4)
        self.assertTrue("5" in dim["lag-members"])
        self.assertTrue("6" in dim["lag-members"])
        self.assertTrue("7" in dim["lag-members"])
        self.assertTrue("8" in dim["lag-members"])
        self.assertTrue("port" in dim)
        self.assertEqual(dim["port"], "2")
        self.assertTrue("dst-lag-member" in dim)
        self.assertEqual(dim["dst-lag-member"], "7")
        self.assertTrue("fabric-trunk-id" in dim)
        self.assertEqual(dim["fabric-trunk-id"], "9")
        self.assertTrue("fabric-trunk-members" in dim)
        self.assertEqual(len(dim["fabric-trunk-members"]), 3)
        self.assertTrue("57" in dim["fabric-trunk-members"])
        self.assertTrue("58" in dim["fabric-trunk-members"])
        self.assertTrue("59" in dim["fabric-trunk-members"])

    def test_packet_trace_ecmp_resolution_1(self):
        rep = PTParser()
        rep.process(self.packet_trace_ecmp_resolution_1)
        serializer = PTToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 4)

        self.assertTrue("timestamp" in data[0])
        timestamp = int(data[0]["timestamp"]) / 1000
        self.assertTrue("name" in data[0])
        self.assertTrue("dimensions" in data[0])
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.packet_trace_ecmp_resolution_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data[0]["name"], "broadview.pt.packet-trace-ecmp-resolution")
        dim = data[0]["dimensions"]
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.packet_trace_profile_1["asic-id"])
        self.assertTrue("ecmp-dst-member" in dim)
        self.assertEqual(dim["ecmp-dst-member"], "100005")
        self.assertTrue("bv-agent" in dim)
        self.assertTrue("ecmp-next-hop-ip" in dim)
        self.assertEqual(dim["ecmp-next-hop-ip"], "1.6.6.2")
        self.assertTrue("ecmp-dst-port" in dim)
        self.assertEqual(dim["ecmp-dst-port"], "11")
        self.assertTrue("ecmp-members" in dim)
        self.assertEqual(len(dim["ecmp-members"]), 2)
        mem = dim["ecmp-members"][0]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "1.2.2.2")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "100004")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "18")
        mem = dim["ecmp-members"][1]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "1.6.6.1")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "100005")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "11")
        self.assertTrue("ecmp-group-id" in dim)
        self.assertEqual(dim["ecmp-group-id"], "100256")
        self.assertTrue("port" in dim)
        self.assertEqual(dim["port"], "1")

        self.assertTrue("timestamp" in data[1])
        timestamp = int(data[1]["timestamp"]) / 1000
        self.assertTrue("name" in data[1])
        self.assertTrue("dimensions" in data[1])
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.packet_trace_ecmp_resolution_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        dim = data[1]["dimensions"]
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.packet_trace_profile_1["asic-id"])
        self.assertTrue("ecmp-dst-member" in dim)
        self.assertEqual(dim["ecmp-dst-member"], "200001")
        self.assertTrue("bv-agent" in dim)
        self.assertTrue("ecmp-next-hop-ip" in dim)
        self.assertEqual(dim["ecmp-next-hop-ip"], "2.3.3.2")
        self.assertTrue("ecmp-dst-port" in dim)
        self.assertEqual(dim["ecmp-dst-port"], "21")
        self.assertTrue("ecmp-members" in dim)
        self.assertEqual(len(dim["ecmp-members"]), 2)
        mem = dim["ecmp-members"][0]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "2.3.3.1")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "200001")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "21")
        mem = dim["ecmp-members"][1]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "2.7.7.2")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "200002")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "21")
        self.assertTrue("ecmp-group-id" in dim)
        self.assertEqual(dim["ecmp-group-id"], "200100")
        self.assertTrue("port" in dim)
        self.assertEqual(dim["port"], "1")

        self.assertTrue("timestamp" in data[2])
        timestamp = int(data[2]["timestamp"]) / 1000
        self.assertTrue("name" in data[2])
        self.assertTrue("dimensions" in data[2])
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.packet_trace_ecmp_resolution_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        dim = data[2]["dimensions"]
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.packet_trace_profile_1["asic-id"])
        self.assertTrue("ecmp-dst-member" in dim)
        self.assertEqual(dim["ecmp-dst-member"], "300005")
        self.assertTrue("bv-agent" in dim)
        self.assertTrue("ecmp-next-hop-ip" in dim)
        self.assertEqual(dim["ecmp-next-hop-ip"], "3.6.6.2")
        self.assertTrue("ecmp-dst-port" in dim)
        self.assertEqual(dim["ecmp-dst-port"], "31")
        self.assertTrue("ecmp-members" in dim)
        self.assertEqual(len(dim["ecmp-members"]), 2)
        mem = dim["ecmp-members"][0]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "3.3.3.1")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "300001")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "38")
        mem = dim["ecmp-members"][1]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "3.7.7.2")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "300002")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "31")
        self.assertTrue("ecmp-group-id" in dim)
        self.assertEqual(dim["ecmp-group-id"], "300100")
        self.assertTrue("port" in dim)
        self.assertEqual(dim["port"], "2")

        self.assertTrue("timestamp" in data[3])
        timestamp = int(data[3]["timestamp"]) / 1000
        self.assertTrue("name" in data[3])
        self.assertTrue("dimensions" in data[3])
        t1 = datetime.datetime.fromtimestamp(timestamp)
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.packet_trace_ecmp_resolution_1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        dim = data[3]["dimensions"]
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.packet_trace_profile_1["asic-id"])
        self.assertTrue("ecmp-dst-member" in dim)
        self.assertEqual(dim["ecmp-dst-member"], "400001")
        self.assertTrue("bv-agent" in dim)
        self.assertTrue("ecmp-next-hop-ip" in dim)
        self.assertEqual(dim["ecmp-next-hop-ip"], "4.3.3.2")
        self.assertTrue("ecmp-dst-port" in dim)
        self.assertEqual(dim["ecmp-dst-port"], "41")
        self.assertTrue("ecmp-members" in dim)
        self.assertEqual(len(dim["ecmp-members"]), 2)
        mem = dim["ecmp-members"][0]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "4.3.3.1")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "400001")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "48")
        mem = dim["ecmp-members"][1]
        self.assertTrue("ip" in mem)
        self.assertEqual(mem["ip"], "4.7.7.2")
        self.assertTrue("id" in mem)
        self.assertEqual(mem["id"], "400002")
        self.assertTrue("port" in mem)
        self.assertEqual(mem["port"], "41")
        self.assertTrue("ecmp-group-id" in dim)
        self.assertEqual(dim["ecmp-group-id"], "400100")
        self.assertTrue("port" in dim)
        self.assertEqual(dim["port"], "2")

    def test_packet_trace_drop_reason(self):
        rep = PTParser()
        rep.process(self.packet_trace_drop_reason_1)
        serializer = PTToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        for x in data:
            self.assertTrue("timestamp" in x)
            self.assertTrue("name" in x)
            self.assertTrue("dimensions" in x)
            self.assertEqual(x["name"], "broadview.pt.packet-trace-drop-reason")
            dim = x["dimensions"]
            if i == 0:
                self.assertEqual(dim["reason"], "l2-lookup-failure")
                l = dim["port-list"]
                self.assertEqual(len(l), 4)
                self.assertEqual(l[0], "1")
                self.assertEqual(l[1], "5")
                self.assertEqual(l[2], "6")
                self.assertEqual(l[3], "10-15")
                self.assertEqual(dim["send-dropped-packet"], 0)
                self.assertEqual(dim["trace-profile"], 0)
                self.assertEqual(dim["packet-threshold"], 0)
                self.assertEqual(x["value"], 4)
            else:
                self.assertEqual(dim["reason"], "vlan-mismatch")
                l = dim["port-list"]
                self.assertEqual(len(l), 4)
                self.assertEqual(l[0], "11")
                self.assertEqual(l[1], "15")
                self.assertEqual(l[2], "16")
                self.assertEqual(l[3], "20-25")
                self.assertEqual(dim["send-dropped-packet"], 1)
                self.assertEqual(dim["trace-profile"], 1)
                self.assertEqual(dim["packet-threshold"], 10)
                self.assertEqual(x["value"], 3)
            i = i + 1

    def test_packet_trace_drop_counter_report(self):
        rep = PTParser()
        rep.process(self.packet_trace_drop_counter_report_1)
        serializer = PTToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 18)
        i = 0
        for x in data:
            self.assertTrue("timestamp" in x)
            self.assertTrue("name" in x)
            self.assertTrue("dimensions" in x)
            self.assertEqual(x["name"], "broadview.pt.packet-trace-drop-counter-report")
            dim = x["dimensions"]
            if i == 0:
                self.assertEqual(dim["realm"], "vlan-xlate-miss-drop")
                self.assertEqual(dim["port"], "1")
                self.assertEqual(x["value"], 10) 
            elif i == 1:
                self.assertEqual(dim["realm"], "vlan-xlate-miss-drop")
                self.assertEqual(dim["port"], "5")
                self.assertEqual(x["value"], 20) 
            elif i == 2:
                self.assertEqual(dim["realm"], "vlan-xlate-miss-drop")
                self.assertEqual(dim["port"], "6")
                self.assertEqual(x["value"], 30) 
            elif i == 3:
                self.assertEqual(dim["realm"], "vlan-xlate-miss-drop")
                self.assertEqual(dim["port"], "10")
                self.assertEqual(x["value"], 40) 
            elif i == 4:
                self.assertEqual(dim["realm"], "vlan-xlate-miss-drop")
                self.assertEqual(dim["port"], "11")
                self.assertEqual(x["value"], 50) 
            elif i == 5:
                self.assertEqual(dim["realm"], "vlan-xlate-miss-drop")
                self.assertEqual(dim["port"], "12")
                self.assertEqual(x["value"], 60) 
            elif i == 6:
                self.assertEqual(dim["realm"], "bpdu-drop")
                self.assertEqual(dim["port"], "1")
                self.assertEqual(x["value"], 70) 
            elif i == 7:
                self.assertEqual(dim["realm"], "bpdu-drop")
                self.assertEqual(dim["port"], "5")
                self.assertEqual(x["value"], 20) 
            elif i == 8:
                self.assertEqual(dim["realm"], "bpdu-drop")
                self.assertEqual(dim["port"], "6")
                self.assertEqual(x["value"], 30) 
            elif i == 9:
                self.assertEqual(dim["realm"], "bpdu-drop")
                self.assertEqual(dim["port"], "10")
                self.assertEqual(x["value"], 40) 
            elif i == 10:
                self.assertEqual(dim["realm"], "bpdu-drop")
                self.assertEqual(dim["port"], "11")
                self.assertEqual(x["value"], 80) 
            elif i == 11:
                self.assertEqual(dim["realm"], "bpdu-drop")
                self.assertEqual(dim["port"], "12")
                self.assertEqual(x["value"], 90) 
            elif i == 12:
                self.assertEqual(dim["realm"], "trill-slowpath-drop")
                self.assertEqual(dim["port"], "1")
                self.assertEqual(x["value"], 10) 
            elif i == 13:
                self.assertEqual(dim["realm"], "trill-slowpath-drop")
                self.assertEqual(dim["port"], "5")
                self.assertEqual(x["value"], 20) 
            elif i == 14:
                self.assertEqual(dim["realm"], "trill-slowpath-drop")
                self.assertEqual(dim["port"], "6")
                self.assertEqual(x["value"], 30) 
            elif i == 15:
                self.assertEqual(dim["realm"], "trill-slowpath-drop")
                self.assertEqual(dim["port"], "10")
                self.assertEqual(x["value"], 40) 
            elif i == 16:
                self.assertEqual(dim["realm"], "trill-slowpath-drop")
                self.assertEqual(dim["port"], "11")
                self.assertEqual(x["value"], 50) 
            elif i == 17:
                self.assertEqual(dim["realm"], "trill-slowpath-drop")
                self.assertEqual(dim["port"], "12")
                self.assertEqual(x["value"], 60) 
            i = i + 1

    def test_packet_trace_supported_drop_reasons(self):
        rep = PTParser()
        rep.process(self.packet_trace_supported_drop_reasons_1)
        serializer = PTToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        d = data[0]
        self.assertTrue("timestamp" in d)
        self.assertTrue("name" in d)
        self.assertTrue("dimensions" in d)
        self.assertEqual(d["name"], "broadview.pt.packet-trace-supported-drop-reasons")
        dim = d["dimensions"]
        self.assertTrue("reasons" in dim)
        self.assertEqual(len(dim["reasons"]), 2)
        self.assertEqual(dim["reasons"][0], "l2-lookup-failure")
        self.assertEqual(dim["reasons"][1], "vlan-mismatch")

if __name__ == "__main__":
    unittest.main()

