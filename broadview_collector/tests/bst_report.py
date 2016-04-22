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
import unittest

# Change these to the host and port the collector is listening on

host = "10.14.244.207"
port = 8082

'''
To see list of metrics in Monasca after this test is run (assuming
the Monasca plugin is enabled (see the README.md file)):

$ monasca --os-username mini-mon --os-password password metric-list | grep broadview

To view an individual statistic, use metric-statistics, as this example:

#monasca --os-username mini-mon --os-password password metric-statistics --dimensions "stat=um-share-buffer-count, service-pool=6, port=3" broadview.bst.ingress-port-service-pool MIN "2016-03-01T00:00:00Z"

This program will display the UTC time associated with the metric, which
can be used to determine an appropriate time argument for the 
metric-statistics command.
'''

class TestBSTCollector(unittest.TestCase):

    def setUp(self):
        # convert datetime string to monasca timestamp

        print("{} UTC".format(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")))
        d = str(datetime.datetime.now()).split(" ")
        t = d[1].split(".")[0]
        d = "{} - {}".format(d[0], t)
        print("Setting timestamp to {}".format(d))
        self.bst_report = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": d,
            "report": [
                {
                    "realm": "device",
                    "data": 46
                }, {
                    "realm": "ingress-port-priority-group",
                    "data": [{
                            "port": "2",
                            "data": [[5, 45500, 44450]]
                        }, {
                            "port": "3",
                            "data": [[6, 25500, 24450]]
                        }]
                }, {
                    "realm": "ingress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 324]]
                        }, {
                            "port": "3",
                            "data": [[6, 366]]
                        }]
                }, {
                    "realm": "ingress-service-pool",
                    "data": [[1, 3240], [2, 3660]]
                }, {
                    "realm": "egress-cpu-queue",
                    "data": [[3, 4566, 0]]
                }, {
                    "realm": "egress-mc-queue",
                    "data": [[1, "1", 34, 89], [2, "4", 1244, 0], [3, "5", 0, 3]]

                }, {
                    "realm": "egress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 0, 324, 0]]
                        }, {
                            "port": "3",
                            "data": [[6, 0, 366, 0]]
                        }]
                }, {
                    "realm": "egress-rqe-queue",
                    "data": [[2, 3333, 4444], [5, 25, 45]]
                }, {
                    "realm": "egress-service-pool",
                    "data": [[2, 0, 0, 3240], [3, 3660, 0, 0]]
                }, {
                    "realm": "egress-uc-queue",
                    "data": [[6, "0", 1111]]
                }, {
                    "realm": "egress-uc-queue-group",
                    "data": [[6, 2222]]
                }]
        }

        self.bst_report_unknown_method = {
            "jsonrpc": "2.0",
            "method": "get-foo-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": d,
            "report": [
                {
                    "realm": "device",
                    "data": 46
                }, {
                    "realm": "ingress-port-priority-group",
                    "data": [{
                            "port": "2",
                            "data": [[5, 45500, 44450]]
                        }, {
                            "port": "3",
                            "data": [[6, 25500, 24450]]
                        }]
                }, {
                    "realm": "ingress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 324]]
                        }, {
                            "port": "3",
                            "data": [[6, 366]]
                        }]
                }, {
                    "realm": "ingress-service-pool",
                    "data": [[1, 3240], [2, 3660]]
                }, {
                    "realm": "egress-cpu-queue",
                    "data": [[3, 4566, 0]]
                }, {
                    "realm": "egress-mc-queue",
                    "data": [[1, "1", 34, 89], [2, "4", 1244, 0], [3, "5", 0, 3]]

                }, {
                    "realm": "egress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 0, 324, 0]]
                        }, {
                            "port": "3",
                            "data": [[6, 0, 366, 0]]
                        }]
                }, {
                    "realm": "egress-rqe-queue",
                    "data": [[2, 3333, 4444], [5, 25, 45]]
                }, {
                    "realm": "egress-service-pool",
                    "data": [[2, 0, 0, 3240], [3, 3660, 0, 0]]
                }, {
                    "realm": "egress-uc-queue",
                    "data": [[6, "0", 1111]]
                }, {
                    "realm": "egress-uc-queue-group",
                    "data": [[6, 2222]]
                }]
        }

        self.bst_report_unknown_realm = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": d,
            "report": [
                {
                    "realm": "mustard",
                    "data": 46
                }]
        }


        self.bst_report_bad_timestamp = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": "xxxxxx ",
            "report": [
                {
                    "realm": "device",
                    "data": 46
                }, {
                    "realm": "ingress-port-priority-group",
                    "data": [{
                            "port": "2",
                            "data": [[5, 45500, 44450]]
                        }, {
                            "port": "3",
                            "data": [[6, 25500, 24450]]
                        }]
                }, {
                    "realm": "ingress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 324]]
                        }, {
                            "port": "3",
                            "data": [[6, 366]]
                        }]
                }, {
                    "realm": "ingress-service-pool",
                    "data": [[1, 3240], [2, 3660]]
                }, {
                    "realm": "egress-cpu-queue",
                    "data": [[3, 4566, 0]]
                }, {
                    "realm": "egress-mc-queue",
                    "data": [[1, "1", 34, 89], [2, "4", 1244, 0], [3, "5", 0, 3]]

                }, {
                    "realm": "egress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 0, 324, 0]]
                        }, {
                            "port": "3",
                            "data": [[6, 0, 366, 0]]
                        }]
                }, {
                    "realm": "egress-rqe-queue",
                    "data": [[2, 3333, 4444], [5, 25, 45]]
                }, {
                    "realm": "egress-service-pool",
                    "data": [[2, 0, 0, 3240], [3, 3660, 0, 0]]
                }, {
                    "realm": "egress-uc-queue",
                    "data": [[6, "0", 1111]]
                }, {
                    "realm": "egress-uc-queue-group",
                    "data": [[6, 2222]]
                }]
        }


        self.bst_report_report_dict = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": d,
            "report": {}
        }


        self.bst_report_empty_report = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": d,
            "report": []
        }


        self.bst_report_missing_report = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": d,
        }


    def test_good_bst(self):
        j = json.dumps(self.bst_report)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
        self.assertEqual(r.status_code, 200)

    def test_unknown_method_bst(self):
        j = json.dumps(self.bst_report_unknown_method)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
        self.assertEqual(r.status_code, 404)

    def test_unknown_realm(self):
        j = json.dumps(self.bst_report_unknown_realm)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
        self.assertEqual(r.status_code, 404)

    def test_bad_timestamp(self):
        j = json.dumps(self.bst_report_bad_timestamp)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
        self.assertEqual(r.status_code, 404)

    def test_report_dict(self):
        j = json.dumps(self.bst_report_report_dict)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
        self.assertEqual(r.status_code, 404)

    def test_empty_report(self):
        j = json.dumps(self.bst_report_empty_report)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
        self.assertEqual(r.status_code, 404)

    def test_missing_report(self):
        j = json.dumps(self.bst_report_missing_report)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
        self.assertEqual(r.status_code, 404)

if __name__ == "__main__":
    unittest.main()


