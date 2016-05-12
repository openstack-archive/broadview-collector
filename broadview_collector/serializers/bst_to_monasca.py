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


class BSTToMonasca(BroadViewSerializerBase):
    '''
    Class that converts BST object model to OpeStack Monasca metrics.
    See broadview-collector/doc/bst_to_monasca_serializer.md for documentation
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
            m["name"] = "broadview.bst." + repr(x)
            m["timestamp"] = timestamp
            m["dimensions"] = {}
            m["dimensions"]["asic-id"] = asic
            m["dimensions"]["bv-agent"] = host
            m["value"] = x.getValue()
            ret.append(m)

        d = data.getIngressPortPriorityGroup() 
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = y.getPort()
                m["dimensions"]["priority-group"] = y.getPriorityGroup()
                m["dimensions"]["stat"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = y.getPort()
                m["dimensions"]["priority-group"] = y.getPriorityGroup()
                m["dimensions"]["stat"] = "um-headroom-buffer-count"
                m["value"] = y.getUmHeadroomBufferCount()
                ret.append(m)

        d = data.getIngressPortServicePool()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = y.getPort()
                m["dimensions"]["service-pool"] = y.getServicePool()
                m["dimensions"]["stat"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

        d = data.getIngressServicePool()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["service-pool"] = y.getServicePool()
                m["dimensions"]["stat"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

        d = data.getEgressCPUQueue()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["queue"] = y.getQueue()
                m["dimensions"]["stat"] = "cpu-buffer-count"
                m["value"] = y.getCPUBufferCount()
                ret.append(m)

                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["queue"] = y.getQueue()
                m["dimensions"]["stat"] = "cpu-queue-entries"
                m["value"] = y.getCPUQueueEntries()
                ret.append(m)

        d = data.getEgressMcQueue()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = y.getPort()
                m["dimensions"]["queue"] = y.getQueue()
                m["dimensions"]["stat"] = "mc-buffer-count"
                m["value"] = y.getMCBufferCount()
                ret.append(m)

                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = y.getPort()
                m["dimensions"]["queue"] = y.getQueue()
                m["dimensions"]["stat"] = "mc-queue-entries"
                m["value"] = y.getMCQueueEntries()
                ret.append(m)

        d = data.getEgressPortServicePool()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = y.getPort()
                m["dimensions"]["service-pool"] = y.getServicePool()
                m["dimensions"]["stat"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = y.getPort()
                m["dimensions"]["service-pool"] = y.getServicePool()
                m["dimensions"]["stat"] = "mc-share-buffer-count"
                m["value"] = y.getMCShareBufferCount()
                ret.append(m)

                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = y.getPort()
                m["dimensions"]["service-pool"] = y.getServicePool()
                m["dimensions"]["stat"] = "mc-share-queue-entries"
                m["value"] = y.getMCShareQueueEntries()
                ret.append(m)

        d = data.getEgressRQEQueue()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["queue"] = y.getQueue()
                m["dimensions"]["stat"] = "rqe-buffer-count"
                m["value"] = y.getRQEBufferCount()
                ret.append(m)

                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["queue"] = y.getQueue()
                m["dimensions"]["stat"] = "rqe-queue-entries"
                m["value"] = y.getRQEQueueEntries()
                ret.append(m)

        d = data.getEgressServicePool()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["service-pool"] = y.getServicePool()
                m["dimensions"]["stat"] = "um-share-buffer-count"
                m["value"] = y.getUmShareBufferCount()
                ret.append(m)

                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["service-pool"] = y.getServicePool()
                m["dimensions"]["stat"] = "mc-share-buffer-count"
                m["value"] = y.getMCShareBufferCount()
                ret.append(m)

                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["service-pool"] = y.getServicePool()
                m["dimensions"]["stat"] = "mc-share-queue-entries"
                m["value"] = y.getMCShareQueueEntries()
                ret.append(m)

        d = data.getEgressUcQueue()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["port"] = y.getPort()
                m["dimensions"]["queue"] = y.getQueue()
                m["dimensions"]["stat"] = "uc-queue-buffer-count"
                m["value"] = y.getUcQueueBufferCount()
                ret.append(m)

        d = data.getEgressUcQueueGroup()
        for x in d:
            for y in x:
                m = {}
                m["name"] = "broadview.bst." + repr(x)
                m["timestamp"] = timestamp
                m["dimensions"] = {}
                m["dimensions"]["asic-id"] = asic
                m["dimensions"]["bv-agent"] = host
                m["dimensions"]["queue-group"] = y.getQueueGroup()
                m["dimensions"]["stat"] = "uc-buffer-count"
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
        # serialize a parsed BST report to Monasca metrics
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
        return "BST To Monasca Serializer" 

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
        serializer = BSTToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        data = data[0]
        self.assertTrue("timestamp" in data)
        data["timestamp"] = data["timestamp"] / 1000
        self.assertTrue("name" in data)
        self.assertTrue("value" in data)
        self.assertTrue("dimensions" in data)
        t1 = datetime.datetime.fromtimestamp(int(data["timestamp"]))
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.bst_report1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data["name"], "broadview.bst.device")
        self.assertEqual(data["value"], 46)
        dim = data["dimensions"]
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.bst_report1["asic-id"])


    def test_bst_report2(self):
        rep = BSTParser()
        rep.process(self.bst_report2)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.ingress-port-priority-group")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("priority-group" in dim)
            self.assertTrue("port" in dim)
            if dim["port"] == "2":
                self.assertEqual(dim["priority-group"], 5)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 45500)
                elif dim["stat"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 44450)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["port"] == "3":
                self.assertEqual(dim["priority-group"], 6)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 25500)
                elif dim["stat"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 24450)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["port"] == True)
            

    def test_bst_report3(self):
        rep = BSTParser()
        rep.process(self.bst_report3)
        serializer = BSTToMonasca()
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
            self.assertTrue("value" in x)
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]) / 1000)
            x["timestamp"] = x["timestamp"] / 1000
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.ingress-port-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            self.assertTrue("port" in dim)
            if dim["port"] == "2":
                self.assertEqual(dim["service-pool"], 5)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["port"] == "3":
                self.assertEqual(dim["service-pool"], 6)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["port"] == True)

    def test_bst_report4(self):
        rep = BSTParser()
        rep.process(self.bst_report4)
        serializer = BSTToMonasca()
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
            self.assertTrue("value" in x)
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.ingress-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            if dim["service-pool"] == 1:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["service-pool"] == 2:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["service-pool"] == True)


    def test_bst_report5(self):
        rep = BSTParser()
        rep.process(self.bst_report5)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-cpu-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            if dim["queue"] == 3:
                if dim["stat"] == "cpu-buffer-count":
                    self.assertTrue(x["value"] == 4566)
                elif dim["stat"] == "cpu-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_bst_report6(self):
        rep = BSTParser()
        rep.process(self.bst_report6)
        serializer = BSTToMonasca()
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
            self.assertTrue("value" in x)
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-mc-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            self.assertTrue("port" in dim)
            if dim["queue"] == 1:
                self.assertTrue(dim["port"] == "1")
                if dim["stat"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 34)
                elif dim["stat"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 89)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["queue"] == 2:
                self.assertTrue(dim["port"] == "4")
                if dim["stat"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 1244)
                elif dim["stat"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["queue"] == 3:
                self.assertTrue(dim["port"] == "5")
                if dim["stat"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 3)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_bst_report7(self):
        rep = BSTParser()
        rep.process(self.bst_report7)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-port-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            self.assertTrue("port" in dim)
            if dim["service-pool"] == 5:
                self.assertTrue(dim["port"] == "2")
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["service-pool"] == 6:
                self.assertTrue(dim["port"] == "3")
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["service-pool"] == True)

    def test_bst_report8(self):
        rep = BSTParser()
        rep.process(self.bst_report8)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-rqe-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            if dim["queue"] == 2:
                if dim["stat"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 3333)
                elif dim["stat"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 4444)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["queue"] == 5:
                if dim["stat"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 25)
                elif dim["stat"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 45)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_bst_report9(self):
        rep = BSTParser()
        rep.process(self.bst_report9)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            if dim["service-pool"] == 2:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["service-pool"] == 3:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["service-pool"] == True)

    def test_bst_report10(self):
        rep = BSTParser()
        rep.process(self.bst_report10)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-uc-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            self.assertTrue("port" in dim)
            if dim["queue"] == 6:
                self.assertEqual(dim["port"], "0")
                if dim["stat"] == "uc-queue-buffer-count":
                    self.assertTrue(x["value"] == 1111)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_bst_report11(self):
        rep = BSTParser()
        rep.process(self.bst_report11)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-uc-queue-group")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue-group" in dim)
            if dim["queue-group"] == 6:
                if dim["stat"] == "uc-buffer-count":
                    self.assertTrue(x["value"] == 2222)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue-group"] == True)

    def test_trigger1(self):
        rep = BSTParser()
        rep.process(self.trigger1)
        serializer = BSTToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        data = data[0]
        self.assertTrue("timestamp" in data)
        data["timestamp"] = data["timestamp"] / 1000
        self.assertTrue("name" in data)
        self.assertTrue("value" in data)
        self.assertTrue("dimensions" in data)
        t1 = datetime.datetime.fromtimestamp(int(data["timestamp"]))
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.trigger1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data["name"], "broadview.bst.device")
        self.assertEqual(data["value"], 46)
        dim = data["dimensions"]
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.trigger1["asic-id"])


    def test_trigger2(self):
        rep = BSTParser()
        rep.process(self.trigger2)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.ingress-port-priority-group")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("priority-group" in dim)
            self.assertTrue("port" in dim)
            if dim["port"] == "2":
                self.assertEqual(dim["priority-group"], 5)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 45500)
                elif dim["stat"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 44450)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["port"] == "3":
                self.assertEqual(dim["priority-group"], 6)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 25500)
                elif dim["stat"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 24450)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["port"] == True)
            

    def test_trigger3(self):
        rep = BSTParser()
        rep.process(self.trigger3)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.ingress-port-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            self.assertTrue("port" in dim)
            if dim["port"] == "2":
                self.assertEqual(dim["service-pool"], 5)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["port"] == "3":
                self.assertEqual(dim["service-pool"], 6)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["port"] == True)

    def test_trigger4(self):
        rep = BSTParser()
        rep.process(self.trigger4)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.ingress-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            if dim["service-pool"] == 1:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["service-pool"] == 2:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["service-pool"] == True)


    def test_trigger5(self):
        rep = BSTParser()
        rep.process(self.trigger5)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-cpu-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            if dim["queue"] == 3:
                if dim["stat"] == "cpu-buffer-count":
                    self.assertTrue(x["value"] == 4566)
                elif dim["stat"] == "cpu-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_trigger6(self):
        rep = BSTParser()
        rep.process(self.trigger6)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-mc-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            self.assertTrue("port" in dim)
            if dim["queue"] == 1:
                self.assertTrue(dim["port"] == "1")
                if dim["stat"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 34)
                elif dim["stat"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 89)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["queue"] == 2:
                self.assertTrue(dim["port"] == "4")
                if dim["stat"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 1244)
                elif dim["stat"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["queue"] == 3:
                self.assertTrue(dim["port"] == "5")
                if dim["stat"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 3)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_trigger7(self):
        rep = BSTParser()
        rep.process(self.trigger7)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-port-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            self.assertTrue("port" in dim)
            if dim["service-pool"] == 5:
                self.assertTrue(dim["port"] == "2")
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["service-pool"] == 6:
                self.assertTrue(dim["port"] == "3")
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["service-pool"] == True)

    def test_trigger8(self):
        rep = BSTParser()
        rep.process(self.trigger8)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-rqe-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            if dim["queue"] == 2:
                if dim["stat"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 3333)
                elif dim["stat"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 4444)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["queue"] == 5:
                if dim["stat"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 25)
                elif dim["stat"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 45)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_trigger9(self):
        rep = BSTParser()
        rep.process(self.trigger9)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            if dim["service-pool"] == 2:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["service-pool"] == 3:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["service-pool"] == True)

    def test_trigger10(self):
        rep = BSTParser()
        rep.process(self.trigger10)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-uc-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            self.assertTrue("port" in dim)
            if dim["queue"] == 6:
                self.assertEqual(dim["port"], "0")
                if dim["stat"] == "uc-queue-buffer-count":
                    self.assertTrue(x["value"] == 1111)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_trigger11(self):
        rep = BSTParser()
        rep.process(self.trigger11)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-uc-queue-group")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue-group" in dim)
            if dim["queue-group"] == 6:
                if dim["stat"] == "uc-buffer-count":
                    self.assertTrue(x["value"] == 2222)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue-group"] == True)

    def test_thresholds1(self):
        rep = BSTParser()
        rep.process(self.thresholds1)
        serializer = BSTToMonasca()
        ret = serializer.serialize(self._host, rep)
        self.assertEqual(ret[0], True)
        data = json.loads(ret[1])
        self.assertTrue(len(data) == 1)
        data = data[0]
        self.assertTrue("timestamp" in data)
        data["timestamp"] = data["timestamp"] / 1000
        self.assertTrue("name" in data)
        self.assertTrue("value" in data)
        self.assertTrue("dimensions" in data)
        t1 = datetime.datetime.fromtimestamp(int(data["timestamp"]))
        t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
        t2 = self.thresholds1["time-stamp"].strip()
        self.assertEqual(t1, t2)
        self.assertEqual(data["name"], "broadview.bst.device")
        self.assertEqual(data["value"], 46)
        dim = data["dimensions"]
        self.assertTrue("asic-id" in dim)
        self.assertEqual(dim["asic-id"], self.thresholds1["asic-id"])


    def test_thresholds2(self):
        rep = BSTParser()
        rep.process(self.thresholds2)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.ingress-port-priority-group")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("priority-group" in dim)
            self.assertTrue("port" in dim)
            if dim["port"] == "2":
                self.assertEqual(dim["priority-group"], 5)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 45500)
                elif dim["stat"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 44450)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["port"] == "3":
                self.assertEqual(dim["priority-group"], 6)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 25500)
                elif dim["stat"] == "um-headroom-buffer-count":
                    self.assertTrue(x["value"] == 24450)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["port"] == True)
            

    def test_thresholds3(self):
        rep = BSTParser()
        rep.process(self.thresholds3)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.ingress-port-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            self.assertTrue("port" in dim)
            if dim["port"] == "2":
                self.assertEqual(dim["service-pool"], 5)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["port"] == "3":
                self.assertEqual(dim["service-pool"], 6)
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["port"] == True)

    def test_thresholds4(self):
        rep = BSTParser()
        rep.process(self.thresholds4)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.ingress-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            if dim["service-pool"] == 1:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["service-pool"] == 2:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["service-pool"] == True)


    def test_thresholds5(self):
        rep = BSTParser()
        rep.process(self.thresholds5)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-cpu-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            if dim["queue"] == 3:
                if dim["stat"] == "cpu-buffer-count":
                    self.assertTrue(x["value"] == 4566)
                elif dim["stat"] == "cpu-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_thresholds6(self):
        rep = BSTParser()
        rep.process(self.thresholds6)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-mc-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            self.assertTrue("port" in dim)
            if dim["queue"] == 1:
                self.assertTrue(dim["port"] == "1")
                if dim["stat"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 34)
                elif dim["stat"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 89)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["queue"] == 2:
                self.assertTrue(dim["port"] == "4")
                if dim["stat"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 1244)
                elif dim["stat"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["queue"] == 3:
                self.assertTrue(dim["port"] == "5")
                if dim["stat"] == "mc-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-queue-entries":
                    self.assertTrue(x["value"] == 3)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_thresholds7(self):
        rep = BSTParser()
        rep.process(self.thresholds7)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-port-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            self.assertTrue("port" in dim)
            if dim["service-pool"] == 5:
                self.assertTrue(dim["port"] == "2")
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 324)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["service-pool"] == 6:
                self.assertTrue(dim["port"] == "3")
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 366)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["service-pool"] == True)

    def test_thresholds8(self):
        rep = BSTParser()
        rep.process(self.thresholds8)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-rqe-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            if dim["queue"] == 2:
                if dim["stat"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 3333)
                elif dim["stat"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 4444)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["queue"] == 5:
                if dim["stat"] == "rqe-buffer-count":
                    self.assertTrue(x["value"] == 25)
                elif dim["stat"] == "rqe-queue-entries":
                    self.assertTrue(x["value"] == 45)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_thresholds9(self):
        rep = BSTParser()
        rep.process(self.thresholds9)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-service-pool")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("service-pool" in dim)
            if dim["service-pool"] == 2:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 3240)
                else:
                    self.assertTrue(dim["stat"] == True)
            elif dim["service-pool"] == 3:
                if dim["stat"] == "um-share-buffer-count":
                    self.assertTrue(x["value"] == 3660)
                elif dim["stat"] == "mc-share-buffer-count":
                    self.assertTrue(x["value"] == 0)
                elif dim["stat"] == "mc-share-queue-entries":
                    self.assertTrue(x["value"] == 0)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["service-pool"] == True)

    def test_thresholds10(self):
        rep = BSTParser()
        rep.process(self.thresholds10)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-uc-queue")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue" in dim)
            self.assertTrue("port" in dim)
            if dim["queue"] == 6:
                self.assertEqual(dim["port"], "0")
                if dim["stat"] == "uc-queue-buffer-count":
                    self.assertTrue(x["value"] == 1111)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue"] == True)

    def test_thresholds11(self):
        rep = BSTParser()
        rep.process(self.thresholds11)
        serializer = BSTToMonasca()
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
            self.assertTrue("dimensions" in x)
            t1 = datetime.datetime.fromtimestamp(int(x["timestamp"]))
            t1 = t1.strftime("%Y-%m-%d - %H:%M:%S")
            t2 = y["time-stamp"].strip()
            self.assertEqual(t1, t2)
            self.assertEqual(x["name"], "broadview.bst.egress-uc-queue-group")
            dim = x["dimensions"]
            self.assertEqual(dim["asic-id"], y["asic-id"])
            self.assertTrue("stat" in dim)
            self.assertTrue("queue-group" in dim)
            if dim["queue-group"] == 6:
                if dim["stat"] == "uc-buffer-count":
                    self.assertTrue(x["value"] == 2222)
                else:
                    self.assertTrue(dim["stat"] == True)
            else:
                self.assertTrue(dim["queue-group"] == True)

if __name__ == "__main__":
    unittest.main()

