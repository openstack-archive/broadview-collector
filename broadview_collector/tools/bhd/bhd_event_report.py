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

host = "127.0.0.1"
port = 8082

'''

Program to generate a black hole event report.

'''

class BHDReport():
    def setUp(self):
        # convert datetime string to agent timestamp

        print("{} UTC".format(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")))
        d = str(datetime.datetime.now()).split(" ")
        t = d[1].split(".")[0]
        d = "{} - {}".format(d[0], t)
        print("Setting timestamp to {}".format(d))
        self.black_hole_event_report = {
                "jsonrpc": "2.0",
                "method": "get-black-hole-event-report",
                "asic-id": "1",
                "version": "2",
                "time-stamp": d,
                "report": {
                        "ingress-port": "1",
                        "egress-port-list": ["2",  "3"],
                        "black-holed-packet-count": 100,
                        "sample-packet": "0010203232.."
                }
        }

    def send(self):
	self.setUp()
        j = json.dumps(self.black_hole_event_report)
        r = requests.post('http://{}:{}'.format(host, port), json=j)

def main():
    x = BHDReport()
    x.send()
	
if __name__ == "__main__":
    main()	


