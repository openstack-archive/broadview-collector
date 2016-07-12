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

class PTDropCounterReport(PTSim):

    def __init__(self, host, port):
        super(PTDropCounterReport, self).__init__(host, port)
        self._data = {
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
                            "port": "11",
                            "count": 700
                        },
                        {
                            "port": "15",
                            "count": 200
                        },
                        {
                            "port": "16",
                            "count": 300
                        },
                        {
                            "port": "20",
                            "count": 400
                        },
                        {
                            "port": "21",
                            "count": 800
                        },
                        {
                            "port": "22",
                            "count": 900
                        }
                    ]
                },
                {
                    "realm": "trill-slowpath-drop",
                    "data": [
                        {
                            "port": "51",
                            "count": 310
                        },
                        {
                            "port": "55",
                            "count": 320
                        },
                        {
                            "port": "56",
                            "count": 330
                        },
                        {
                            "port": "60",
                            "count": 340
                        },
                        {
                            "port": "61",
                            "count": 350
                        },
                        {
                            "port": "62",
                            "count": 360
                        }
                    ]
                }

            ]
        }

def usage():
    print "pt_drop_counter_report [-h host] [-p port]"

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

    x = PTDropCounterReport(host, port)
    x.send()
	
if __name__ == "__main__":
    main()	


