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

# Change these to the host and port the collector is listening on

host = "10.14.244.207"
port = 8082

'''

Program to generate a similated microburst.

A great way to use this is from a loop in bash:

while true; do python bst_burst.py ; sleep 90; done

This will make a pretty grafana graph in monasca that simulates 
microbursts.

Feel free to modify the bst_report_burst and bst_report_falloff
dictionaries to similate other data.

TODOS: move the looping into the code, perhaps allow for random
data and range specification.

'''

class BSTMicroburst():

    def setUp(self):
        # convert datetime string to monasca timestamp

        print("{} UTC".format(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")))
        d = str(datetime.datetime.now()).split(" ")
        t = d[1].split(".")[0]
        d = "{} - {}".format(d[0], t)
        print("Setting timestamp to {}".format(d))
        self.bst_report_burst = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": d,
            "report": [
                {
                    "realm": "device",
                    "data": 46000
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
                            "data": [[5, 10000]]
                        }, {
                            "port": "3",
                            "data": [[6, 10000]]
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
                            "data": [[5, 0, 24000, 0]]
                        }, {
                            "port": "3",
                            "data": [[6, 0, 24000, 0]]
                        }]
                }, {
                    "realm": "egress-rqe-queue",
                    "data": [[2, 3333, 4444], [5, 7000, 7000]]
                }, {
                    "realm": "egress-service-pool",
                    "data": [[2, 5700, 4567, 3240], [3, 3660, 8000, 7549]]
                }, {
                    "realm": "egress-uc-queue",
                    "data": [[6, "0", 1111]]
                }, {
                    "realm": "egress-uc-queue-group",
                    "data": [[6, 2222]]
                }]
        }


        self.bst_report_falloff = {
            "jsonrpc": "2.0",
            "method": "get-bst-report",
            "asic-id": "20",
            "version": "1",
            "time-stamp": d,
            "report": [
                {
                    "realm": "device",
                    "data": 15
                }, {
                    "realm": "ingress-port-priority-group",
                    "data": [{
                            "port": "2",
                            "data": [[5, 15, 15]]
                        }, {
                            "port": "3",
                            "data": [[6, 15, 15]]
                        }]
                }, {
                    "realm": "ingress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 15]]
                        }, {
                            "port": "3",
                            "data": [[6, 15]]
                        }]
                }, {
                    "realm": "ingress-service-pool",
                    "data": [[1, 15], [2, 15]]
                }, {
                    "realm": "egress-cpu-queue",
                    "data": [[3, 15, 15]]
                }, {
                    "realm": "egress-mc-queue",
                    "data": [[1, "1", 15, 15], [2, "4", 15, 15], [3, "5", 15, 15]]

                }, {
                    "realm": "egress-port-service-pool",
                    "data": [{
                            "port": "2",
                            "data": [[5, 15, 15, 15]]
                        }, {
                            "port": "3",
                            "data": [[6, 15, 15, 15]]
                        }]
                }, {
                    "realm": "egress-rqe-queue",
                    "data": [[2, 15, 15], [5, 15, 15]]
                }, {
                    "realm": "egress-service-pool",
                    "data": [[2, 15, 15, 15], [3, 15, 15, 15]]
                }, {
                    "realm": "egress-uc-queue",
                    "data": [[6, "15", 15]]
                }, {
                    "realm": "egress-uc-queue-group",
                    "data": [[6, 15]]
                }]
        }

    def burst(self):
	self.setUp()
        j = json.dumps(self.bst_report_burst)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
	time.sleep(10)
	self.setUp()
        j = json.dumps(self.bst_report_burst)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
	time.sleep(10)
	self.setUp()
        j = json.dumps(self.bst_report_falloff)
        r = requests.post('http://{}:{}'.format(host, port), json=j)
	time.sleep(10)
	self.setUp()
        j = json.dumps(self.bst_report_falloff)
        r = requests.post('http://{}:{}'.format(host, port), json=j)

def main():
    x = BSTMicroburst()
    x.burst()
	
if __name__ == "__main__":
    main()	


