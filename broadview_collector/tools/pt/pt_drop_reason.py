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

import getopt
import sys
from pt_sim import PTSim

'''
Program to simulate sending a get-packet-trace-profile message  
from a BroadView agent.

'''

class PTDropReason(PTSim):

    def __init__(self, host, port):
        super(PTDropReason, self).__init__(host, port)
        self._data = {
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
                    "send-dropped-packet": 1,
                    "trace-profile": 0,
                    "packet-count": 3,
                    "packet-threshold": 0
                },
                {
                    "reason": "vlan-mismatch",
                    "port-list": [
                        "2",
                        "10",
                        "12",
                        "20-30"
                    ],
                    "send-dropped-packet": 1,
                    "trace-profile": 1,
                    "packet-count": 6,
                    "packet-threshold": 10
                }
            ],
            "id": 1
        }

def usage():
    print "pt_drop_reason [-h host] [-p port]"

def main():

    host = None
    port = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o == "-h":
            host = a
        elif o == "-p":
            port = a
        else:
            assert False, "unhandled option"

    x = PTDropReason(host, port)
    x.send()
	
if __name__ == "__main__":
    main()	


