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
Program to simulate sending a get-packet-trace-lag-resolution message  
from a BroadView agent.

'''

class PTLAGResolution(PTSim):

    def __init__(self, host, port):
        super(PTLAGResolution, self).__init__(host, port)
        self._data = {
            "jsonrpc": "2.0",
            "method": " get-packet-trace-lag-resolution",
            "asic-id": "1",
            "version": "1",
            "time-stamp": self._timestamp,
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
                        "fabric-trunk-id": "6",
                        "fabric-trunk-members": ["27", "28", "29"],
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
                        "fabric-trunk-id": "6",
                        "fabric-trunk-members": ["27", "28", "29"],
                    }
                }
            ],
            "id": 1
        }

def usage():
    print "pt_lag_resolution [-h host] [-p port]"

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

    x = PTLAGResolution(host, port)
    x.send()
	
if __name__ == "__main__":
    main()	


