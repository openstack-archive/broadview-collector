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
Program to simulate a get-packet-trace-ecmp-resolution message received
from a BroadView agent.

'''

class PTECMPResolution(PTSim):

    def __init__(self, host, port):
        super(PTECMPResolution, self).__init__(host, port)
        self._data = {
            "jsonrpc": "2.0",
            "method": " get-packet-trace-ecmp-resolution",
            "asic-id": "1",
            "version": "1",
            "time-stamp": self._timestamp,
            "report": [
                {
                    "port": "1",
                    "ecmp-link-resolution": [
                        {
                            "ecmp-group-id": "200256",
                            "ecmp-members": [["100004", "2.2.2.2", "28"],["100005", "6.6.6.1", "41"]],
                            "ecmp-dst-member": "100005",
                            "ecmp-dst-port": "41",
                            "ecmp-next-hop-ip": "6.6.6.2"
                        },
                        {
                            "ecmp-group-id": "200100",
                            "ecmp-members": [["100001", "3.3.3.1", "31"], ["100002", "7.7.7.2", "21"]],
                            "ecmp-dst-member": "100001",
                            "ecmp-dst-port": "31",
                            "ecmp-next-hop-ip": "3.3.3.2"
                        }
                    ]
                },
                {
                    "port": "2",
                    "ecmp-link-resolution": [
                        {
                            "ecmp-group-id": "200512",
                            "ecmp-members": [["100002", "6.3.3.1", "61"], ["100004", "9.9.9.2", "41"]],
                            "ecmp-dst-member": "100010",
                            "ecmp-dst-port": "81",
                            "ecmp-next-hop-ip": "7.6.6.2"
                        },
                        {
                            "ecmp-group-id": "200200",
                            "ecmp-members": [["100008", "4.4.4.4", "56"],["100010", "8.8.8.1", "82"]],
                            "ecmp-dst-member": "100002",
                            "ecmp-dst-port": "62",
                            "ecmp-next-hop-ip": "6.5.4.3"
                        }
                    ]
                }
            ],
            "id": 1
        }

def usage():
    print "pt_ecmp_resolution [-h host] [-p port]"

def main():

    host = None
    port = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:")
    except getopt.GetoptError as err:
        print str(err)  
        usage()
        sys.exit(2)
    for o, a in opts:
        if o == "-h":
            host = a
        elif o == "-p":
            port = a
        else:
            assert False, "unhandled option"

    x = PTECMPResolution(host, port)
    x.send()
	
if __name__ == "__main__":
    main()	


