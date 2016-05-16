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
from broadview_lib.bst.bst_parser import BSTParser, ReportTypes
import json
import unittest
import datetime
import time

class BSTToStacklight(BroadViewSerializerBase):
    '''
    Class that converts BST object model to Stacklight metrics 
    '''

    def __init__(self):
        pass

    def __serializeToJSON(self, host, report, data):
        ret = []
        timestamp = time.mktime(data.getTimestamp()) * 1000
        asic = data.getASICId()
        x = data.getDeviceData()

        if x:
            m = {}
            m["entity"] = "broadview-bst"
            m["name"] = repr(x)
            m["timestamp"] = timestamp
            m["asic-id"] = asic
            m["bv-agent"] = host
            m["value"] = x.getValue()
            ret.append(m)

        d = data.getIngressPortPriorityGroup() 
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["port"] = y.getPort()
                m["priority-group"] = y.getPriorityGroup()
                m["metric"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["port"] = y.getPort()
                m["priority-group"] = y.getPriorityGroup()
                m["metric"] = "um-headroom-buffer-count"
                m["value"] = y.getUmHeadroomBufferCount()
                ret.append(m)

        d = data.getIngressPortServicePool()
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst"
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["port"] = y.getPort()
                m["service-pool"] = y.getServicePool()
                m["metric"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

        d = data.getIngressServicePool()
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst"
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["service-pool"] = y.getServicePool()
                m["metric"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

        d = data.getEgressCPUQueue()
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["queue"] = y.getQueue()
                m["metric"] = "cpu-buffer-count"
                m["value"] = y.getCPUBufferCount()
                ret.append(m)

                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["queue"] = y.getQueue()
                m["metric"] = "cpu-queue-entries"
                m["value"] = y.getCPUQueueEntries()
                ret.append(m)

        d = data.getEgressMcQueue()
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["port"] = y.getPort()
                m["queue"] = y.getQueue()
                m["metric"] = "mc-buffer-count"
                m["value"] = y.getMCBufferCount()
                ret.append(m)

                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["bv-agent"] = host
                m["asic-id"] = asic
                m["port"] = y.getPort()
                m["queue"] = y.getQueue()
                m["metric"] = "mc-queue-entries"
                m["value"] = y.getMCQueueEntries()
                ret.append(m)

        d = data.getEgressPortServicePool()
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["bv-agent"] = host
                m["asic-id"] = asic
                m["port"] = y.getPort()
                m["service-pool"] = y.getServicePool()
                m["metric"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["port"] = y.getPort()
                m["service-pool"] = y.getServicePool()
                m["metric"] = "mc-share-buffer-count"
                m["value"] = y.getMCShareBufferCount()
                ret.append(m)

                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["port"] = y.getPort()
                m["service-pool"] = y.getServicePool()
                m["metric"] = "mc-share-queue-entries"
                m["value"] = y.getMCShareQueueEntries()
                ret.append(m)

        d = data.getEgressRQEQueue()
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["queue"] = y.getQueue()
                m["metric"] = "rqe-buffer-count"
                m["value"] = y.getRQEBufferCount()
                ret.append(m)

                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["queue"] = y.getQueue()
                m["metric"] = "rqe-queue-entries"
                m["value"] = y.getRQEQueueEntries()
                ret.append(m)

        d = data.getEgressServicePool()
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["service-pool"] = y.getServicePool()
                m["metric"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["service-pool"] = y.getServicePool()
                m["metric"] = "mc-share-buffer-count"
                m["value"] = y.getMCShareBufferCount()
                ret.append(m)

                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["service-pool"] = y.getServicePool()
                m["metric"] = "mc-share-queue-entries"
                m["value"] = y.getMCShareQueueEntries()
                ret.append(m)

        d = data.getEgressUcQueue()
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["port"] = y.getPort()
                m["queue"] = y.getQueue()
                m["metric"] = "uc-queue-buffer-count"
                m["value"] = y.getUcQueueBufferCount()
                ret.append(m)

        d = data.getEgressUcQueueGroup()
        for x in d:
            for y in x:
                m = {}
                m["entity"] = "broadview-bst" 
                m["name"] = repr(x)
                m["timestamp"] = timestamp
                m["asic-id"] = asic
                m["bv-agent"] = host
                m["queue-group"] = y.getQueueGroup()
                m["metric"] = "uc-buffer-count"
                m["value"] = y.getUcBufferCount()
                ret.append(m)

        return json.dumps(ret)

    def _toReport(self, host, data):
        return self.__serializeToJSON(host, "bst-report", data)

    def _toTrigger(self, host, data):
        return self.__serializeToJSON(host, "bst-trigger", data)

    def _toThreshold(self, host, data):
        return self.__serializeToJSON(host, "bst-thresholds", data)

    def serialize(self, host, data):
        # serialize a parsed BST report to Monasca mtrics
        ret = (False, None)

        rpt = data.getReportType()

        s = None        
        if rpt == ReportTypes.Report:
            s = self._toReport(host, data)
        elif rpt == ReportTypes.Trigger:
            s = self._toTrigger(host, data)
        elif rpt == ReportTypes.Threshold:
            s = self._toThreshold(host, data)

        if s:
            ret = (True, s)

        return ret

    def __repr__(self):
        return "BST To Stacklight Serializer" 

class TestSerializer(unittest.TestCase):

    def setUp(self):
        self._host = "127.0.0.1"
        self.bst_report1 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "device",
                    "data": 46
                }]
        }

        self.bst_report2 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "ingress-port-priority-group",
                    "data": [{
                            "port": "2",
                            "data": [[5, 45500, 44450]]
                        }, {
                            "port": "3",
                            "data": [[6, 25500, 24450]]
                        }]
                }]
        }

        self.bst_report3 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "ingress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 324]]
                        }, {
                            "port": "3",
                            "data": [[6, 366]]
                        }]
                }]
        }

        self.bst_report4 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "ingress-service-pool",
                    "data": [[1, 3240], [2, 3660]]
                }]
        }

        self.bst_report5 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-cpu-queue",
                    "data": [[3, 4566, 0]]
                }]
        }

        self.bst_report6 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-mc-queue",
                    "data": [[1, "1", 34, 89], [2, "4", 1244, 0], [3, "5", 0,
3]]
                }]
        }

        self.bst_report7 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 0, 324, 0]]
                        }, {
                            "port": "3",
                            "data": [[6, 0, 366, 0]]
                        }]
                }]
        }

        self.bst_report8 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-rqe-queue",
                    "data": [[2, 3333, 4444], [5, 25, 45]]
                }]
        }

        self.bst_report9 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-service-pool",
                    "data": [[2, 0, 0, 3240], [3, 3660, 0, 0]]
                }]
        }

        self.bst_report10 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-uc-queue",
                    "data": [[6, "0", 1111]]
                }]
        }

        self.bst_report11 = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-uc-queue-group",
                    "data": [[6, 2222]]
                }]
        }


        self.trigger1 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "device",
                    "data": 46
                }]
        }

        self.trigger2 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "ingress-port-priority-group",

                    "data": [{
                            "port": "2",
                            "data": [[5, 45500, 44450]]
                        }, {
                            "port": "3",
                            "data": [[6, 25500, 24450]]
                        }]
                }]
        }

        self.trigger3 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "ingress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 324]]
                        }, {
                            "port": "3",
                            "data": [[6, 366]]
                        }]
                }]
        }

        self.trigger4 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "ingress-service-pool",
                    "data": [[1, 3240], [2, 3660]]
                }]
        }

        self.trigger5 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "egress-cpu-queue",
                    "data": [[3, 4566, 0]]
                }]
        }

        self.trigger6 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "egress-mc-queue",
                    "data": [[1, "1", 34, 89], [2, "4", 1244, 0], [3, "5", 0,
3]]
                }]
        }

        self.trigger7 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "egress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 0, 324, 0]]
                        }, {
                            "port": "3",
                            "data": [[6, 0, 366, 0]]
                        }]
                }]
        }

        self.trigger8 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "egress-rqe-queue",
                    "data": [[2, 3333, 4444], [5, 25, 45]]
                }]
        }

        self.trigger9 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "egress-service-pool",
                    "data": [[2, 0, 0, 3240], [3, 3660, 0, 0]]
                }]
        }

        self.trigger10 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "egress-uc-queue",
                    "data": [[6, "0", 1111]]
                }]
        }

        self.trigger11 = {
            "jsonrpc": "2.0",
            "method": "trigger-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-18 - 00:13:08 ",
            "realm": "ingress-port-priority-group",
            "counter": "um-share-buffer-count",
            "port": "2",
            "priority-group": "5",
            "report": [
                {
                    "realm": "egress-uc-queue-group",
                    "data": [[6, 2222]]
                }]
        }


        self.thresholds1 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "device",
                    "data": 46
                }]
        }

        self.thresholds2 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "ingress-port-priority-group",
                    "data": [{
                            "port": "2",
                            "data": [[5, 45500, 44450]]
                        }, {
                            "port": "3",
                            "data": [[6, 25500, 24450]]
                        }]
                }]
        }

        self.thresholds3 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "ingress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 324]]
                        }, {
                            "port": "3",
                            "data": [[6, 366]]
                        }]
                }]
        }

        self.thresholds4 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "ingress-service-pool",
                    "data": [[1, 3240], [2, 3660]]
                }]
        }

        self.thresholds5 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-cpu-queue",
                    "data": [[3, 4566, 0]]
                }]
        }

        self.thresholds6 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-mc-queue",
                    "data": [[1, "1", 34, 89], [2, "4", 1244, 0], [3, "5", 0, 3]]
                }]
        }

        self.thresholds7 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 0, 324, 0]]
                        }, {
                            "port": "3",
                            "data": [[6, 0, 366, 0]]
                        }]
                }]
        }

        self.thresholds8 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-rqe-queue",
                    "data": [[2, 3333, 4444], [5, 25, 45]]
                }]
        }

        self.thresholds9 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-service-pool",
                    "data": [[2, 0, 0, 3240], [3, 3660, 0, 0]]
                }]
        }

        self.thresholds10 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-uc-queue",
                    "data": [[6, "0", 1111]]
                }]
        }

        self.thresholds11 = {
            "jsonrpc": "2.0",
            "method": "get-bst-thresholds",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "2014-11-14 - 00:15:04 ",
            "report": [
                {
                    "realm": "egress-uc-queue-group",
                    "data": [[6, 2222]]
                }]
        }


    def test_bst_report1(self):
        rep = BSTParser()
        rep.process(self.bst_report1)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        data = data[0]
        self.assertTrue("timestamp" in data)
        data["timestamp"] = data["timestamp"] / 1000
        self.assertTrue("entity" in data)
        self.assertTrue(data["entity"] == "broadview-bst")
        self.assertTrue("bv-agent" in data)
        self.assertTrue("name" in data)
        self.assertTrue("value" in data)
        t1 = datetime.datetime.fromtimestamp(int(data["timestamp"]))
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.bst_report1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data["name"], "device")
        self.assertEqual(data["value"], 46)
        self.assertTrue("asic-id" in data)
        self.assertEqual(data["asic-id"], self.bst_report1["asic-id"])


    def test_bst_report2(self):
        rep = BSTParser()
        rep.process(self.bst_report2)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 4)
        i = 0
        y = self.bst_report2
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "ingress-port-priority-group")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("priority-group" in x)
            self.assertTrue("port" in x)
            if x["port"] == "2":
                self.assertEqual(x["priority-group"], 5)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 45500)
                elif x["metric"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 44450)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["port"] == "3":
                self.assertEqual(x["priority-group"], 6)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 25500)
                elif x["metric"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 24450)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["port"] == True)
            

    def test_bst_report3(self):
        rep = BSTParser()
        rep.process(self.bst_report3)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        y = self.bst_report3
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            self.assertTrue("name" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]) / 1000)
            x["timestamp"] = x["timestamp"] / 1000
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "ingress-port-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            self.assertTrue("port" in x)
            if x["port"] == "2":
                self.assertEqual(x["service-pool"], 5)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["port"] == "3":
                self.assertEqual(x["service-pool"], 6)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["port"] == True)

    def test_bst_report4(self):
        rep = BSTParser()
        rep.process(self.bst_report4)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        y = self.bst_report4
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "ingress-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            if x["service-pool"] == 1:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["service-pool"] == 2:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["service-pool"] == True)


    def test_bst_report5(self):
        rep = BSTParser()
        rep.process(self.bst_report5)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        y = self.bst_report5
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-cpu-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            if x["queue"] == 3:
                if x["metric"] == "cpu-buffer-count":
                    self.assertTrue(x["value"] == 4566)
                elif x["metric"] == "cpu-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_bst_report6(self):
        rep = BSTParser()
        rep.process(self.bst_report6)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)
        i = 0
        y = self.bst_report6
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-mc-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            self.assertTrue("port" in x)
            if x["queue"] == 1:
                self.assertTrue(x["port"] == "1")
                if x["metric"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 34)
                elif x["metric"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 89)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["queue"] == 2:
                self.assertTrue(x["port"] == "4")
                if x["metric"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 1244)
                elif x["metric"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["queue"] == 3:
                self.assertTrue(x["port"] == "5")
                if x["metric"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 3)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_bst_report7(self):
        rep = BSTParser()
        rep.process(self.bst_report7)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)
        i = 0
        y = self.bst_report7
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-port-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            self.assertTrue("port" in x)
            if x["service-pool"] == 5:
                self.assertTrue(x["port"] == "2")
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["service-pool"] == 6:
                self.assertTrue(x["port"] == "3")
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["service-pool"] == True)

    def test_bst_report8(self):
        rep = BSTParser()
        rep.process(self.bst_report8)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 4)
        i = 0
        y = self.bst_report8
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-rqe-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            if x["queue"] == 2:
                if x["metric"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 3333)
                elif x["metric"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 4444)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["queue"] == 5:
                if x["metric"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 25)
                elif x["metric"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 45)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_bst_report9(self):
        rep = BSTParser()
        rep.process(self.bst_report9)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)
        i = 0
        y = self.bst_report9
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            if x["service-pool"] == 2:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["service-pool"] == 3:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["service-pool"] == True)

    def test_bst_report10(self):
        rep = BSTParser()
        rep.process(self.bst_report10)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        i = 0
        y = self.bst_report10
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-uc-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            self.assertTrue("port" in x)
            if x["queue"] == 6:
                self.assertEqual(x["port"], "0")
                if x["metric"] == "uc-queue-buffer-count":
                    self.assertTrue(x["value"] == 1111)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_bst_report11(self):
        rep = BSTParser()
        rep.process(self.bst_report11)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        i = 0
        y = self.bst_report11
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-uc-queue-group")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue-group" in x)
            if x["queue-group"] == 6:
                if x["metric"] == "uc-buffer-count":
                    self.assertTrue(x["value"] == 2222)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue-group"] == True)

    def test_trigger1(self):
        rep = BSTParser()
        rep.process(self.trigger1)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        data = data[0]
        self.assertTrue("timestamp" in data)
        data["timestamp"] = data["timestamp"] / 1000
        self.assertTrue("name" in data)
        self.assertTrue("value" in data)
        self.assertTrue("entity" in data)
        self.assertTrue(data["entity"] == "broadview-bst")
        self.assertTrue("bv-agent" in data)
        t1 = datetime.datetime.fromtimestamp(int(data["timestamp"]))
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.trigger1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data["name"], "device")
        self.assertEqual(data["value"], 46)
        self.assertTrue("asic-id" in data)
        self.assertEqual(data["asic-id"], self.trigger1["asic-id"])


    def test_trigger2(self):
        rep = BSTParser()
        rep.process(self.trigger2)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 4)
        i = 0
        y = self.trigger2
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "ingress-port-priority-group")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("priority-group" in x)
            self.assertTrue("port" in x)
            if x["port"] == "2":
                self.assertEqual(x["priority-group"], 5)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 45500)
                elif x["metric"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 44450)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["port"] == "3":
                self.assertEqual(x["priority-group"], 6)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 25500)
                elif x["metric"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 24450)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["port"] == True)
            

    def test_trigger3(self):
        rep = BSTParser()
        rep.process(self.trigger3)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        y = self.trigger3
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "ingress-port-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            self.assertTrue("port" in x)
            if x["port"] == "2":
                self.assertEqual(x["service-pool"], 5)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["port"] == "3":
                self.assertEqual(x["service-pool"], 6)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["port"] == True)

    def test_trigger4(self):
        rep = BSTParser()
        rep.process(self.trigger4)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        y = self.trigger4
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "ingress-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            if x["service-pool"] == 1:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["service-pool"] == 2:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["service-pool"] == True)


    def test_trigger5(self):
        rep = BSTParser()
        rep.process(self.trigger5)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        y = self.trigger5
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-cpu-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            if x["queue"] == 3:
                if x["metric"] == "cpu-buffer-count":
                    self.assertTrue(x["value"] == 4566)
                elif x["metric"] == "cpu-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_trigger6(self):
        rep = BSTParser()
        rep.process(self.trigger6)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)
        i = 0
        y = self.trigger6
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-mc-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            self.assertTrue("port" in x)
            if x["queue"] == 1:
                self.assertTrue(x["port"] == "1")
                if x["metric"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 34)
                elif x["metric"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 89)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["queue"] == 2:
                self.assertTrue(x["port"] == "4")
                if x["metric"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 1244)
                elif x["metric"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["queue"] == 3:
                self.assertTrue(x["port"] == "5")
                if x["metric"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 3)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_trigger7(self):
        rep = BSTParser()
        rep.process(self.trigger7)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)
        i = 0
        y = self.trigger7
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-port-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            self.assertTrue("port" in x)
            if x["service-pool"] == 5:
                self.assertTrue(x["port"] == "2")
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["service-pool"] == 6:
                self.assertTrue(x["port"] == "3")
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["service-pool"] == True)

    def test_trigger8(self):
        rep = BSTParser()
        rep.process(self.trigger8)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 4)
        i = 0
        y = self.trigger8
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-rqe-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            if x["queue"] == 2:
                if x["metric"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 3333)
                elif x["metric"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 4444)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["queue"] == 5:
                if x["metric"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 25)
                elif x["metric"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 45)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_trigger9(self):
        rep = BSTParser()
        rep.process(self.trigger9)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)
        i = 0
        y = self.trigger9
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            if x["service-pool"] == 2:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["service-pool"] == 3:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["service-pool"] == True)

    def test_trigger10(self):
        rep = BSTParser()
        rep.process(self.trigger10)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        i = 0
        y = self.trigger10
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-uc-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            self.assertTrue("port" in x)
            if x["queue"] == 6:
                self.assertEqual(x["port"], "0")
                if x["metric"] == "uc-queue-buffer-count":
                    self.assertTrue(x["value"] == 1111)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_trigger11(self):
        rep = BSTParser()
        rep.process(self.trigger11)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        i = 0
        y = self.trigger11
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("entity" in x)
            self.assertTrue("metric" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-uc-queue-group")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue-group" in x)
            if x["queue-group"] == 6:
                if x["metric"] == "uc-buffer-count":
                    self.assertTrue(x["value"] == 2222)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue-group"] == True)

    def test_thresholds1(self):
        rep = BSTParser()
        rep.process(self.thresholds1)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        data = data[0]
        self.assertTrue("timestamp" in data)
        data["timestamp"] = data["timestamp"] / 1000
        self.assertTrue("name" in data)
        self.assertTrue("value" in data)
        self.assertTrue("entity" in data)
        self.assertTrue(data["entity"] == "broadview-bst")
        self.assertTrue("bv-agent" in data)
        t1 = datetime.datetime.fromtimestamp(int(data["timestamp"]))
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.thresholds1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data["name"], "device")
        self.assertEqual(data["value"], 46)
        self.assertTrue("asic-id" in data)
        self.assertEqual(data["asic-id"], self.thresholds1["asic-id"])


    def test_thresholds2(self):
        rep = BSTParser()
        rep.process(self.thresholds2)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 4)
        i = 0
        y = self.thresholds2
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            self.assertTrue("entity" in x)
            self.assertTrue(x["entity"] == "broadview-bst")
            self.assertTrue("bv-agent" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "ingress-port-priority-group")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("priority-group" in x)
            self.assertTrue("port" in x)
            if x["port"] == "2":
                self.assertEqual(x["priority-group"], 5)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 45500)
                elif x["metric"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 44450)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["port"] == "3":
                self.assertEqual(x["priority-group"], 6)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 25500)
                elif x["metric"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 24450)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["port"] == True)
            

    def test_thresholds3(self):
        rep = BSTParser()
        rep.process(self.thresholds3)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        y = self.thresholds3
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "ingress-port-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            self.assertTrue("port" in x)
            if x["port"] == "2":
                self.assertEqual(x["service-pool"], 5)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["port"] == "3":
                self.assertEqual(x["service-pool"], 6)
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["port"] == True)

    def test_thresholds4(self):
        rep = BSTParser()
        rep.process(self.thresholds4)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        y = self.thresholds4
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "ingress-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            if x["service-pool"] == 1:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["service-pool"] == 2:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["service-pool"] == True)


    def test_thresholds5(self):
        rep = BSTParser()
        rep.process(self.thresholds5)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 2)
        i = 0
        y = self.thresholds5
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-cpu-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            if x["queue"] == 3:
                if x["metric"] == "cpu-buffer-count":
                    self.assertTrue(x["value"] == 4566)
                elif x["metric"] == "cpu-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_thresholds6(self):
        rep = BSTParser()
        rep.process(self.thresholds6)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)
        i = 0
        y = self.thresholds6
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-mc-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            self.assertTrue("port" in x)
            if x["queue"] == 1:
                self.assertTrue(x["port"] == "1")
                if x["metric"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 34)
                elif x["metric"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 89)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["queue"] == 2:
                self.assertTrue(x["port"] == "4")
                if x["metric"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 1244)
                elif x["metric"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["queue"] == 3:
                self.assertTrue(x["port"] == "5")
                if x["metric"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 3)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_thresholds7(self):
        rep = BSTParser()
        rep.process(self.thresholds7)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)
        i = 0
        y = self.thresholds7
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-port-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            self.assertTrue("port" in x)
            if x["service-pool"] == 5:
                self.assertTrue(x["port"] == "2")
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["service-pool"] == 6:
                self.assertTrue(x["port"] == "3")
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["service-pool"] == True)

    def test_thresholds8(self):
        rep = BSTParser()
        rep.process(self.thresholds8)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 4)
        i = 0
        y = self.thresholds8
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-rqe-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            if x["queue"] == 2:
                if x["metric"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 3333)
                elif x["metric"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 4444)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["queue"] == 5:
                if x["metric"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 25)
                elif x["metric"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 45)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_thresholds9(self):
        rep = BSTParser()
        rep.process(self.thresholds9)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 6)
        i = 0
        y = self.thresholds9
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-service-pool")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("service-pool" in x)
            if x["service-pool"] == 2:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(x["metric"] == True)
            elif x["service-pool"] == 3:
                if x["metric"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                elif x["metric"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif x["metric"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["service-pool"] == True)

    def test_thresholds10(self):
        rep = BSTParser()
        rep.process(self.thresholds10)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        i = 0
        y = self.thresholds10
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-uc-queue")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue" in x)
            self.assertTrue("port" in x)
            if x["queue"] == 6:
                self.assertEqual(x["port"], "0")
                if x["metric"] == "uc-queue-buffer-count":
                    self.assertTrue(x["value"] == 1111)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue"] == True)

    def test_thresholds11(self):
        rep = BSTParser()
        rep.process(self.thresholds11)
        serializer = BSTToStacklight()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        i = 0
        y = self.thresholds11
        for x in data:
            i = i + 1
            self.assertTrue("timestamp" in x)
            x["timestamp"] = x["timestamp"] / 1000
            self.assertTrue("name" in x)
            self.assertTrue("value" in x)
            self.assertTrue("metric" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "egress-uc-queue-group")
            self.assertEqual(x["asic-id"], y["asic-id"])
            self.assertTrue("metric" in x)
            self.assertTrue("queue-group" in x)
            if x["queue-group"] == 6:
                if x["metric"] == "uc-buffer-count":
                    self.assertTrue(x["value"] == 2222)
                else:
                    self.assertTrue(x["metric"] == True)
            else:
                self.assertTrue(x["queue-group"] == True)

if __name__ == "__main__":
    unittest.main()

