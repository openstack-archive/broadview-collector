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

class PTProfile(PTSim):

    def __init__(self, host, port):
        super(PTProfile, self).__init__(host, port)
        self._data = {
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
                            "data": [
                                {
                                    "ecmp-group-id": "200256",
                                    "ecmp-members": [["100004", "2.2.2.2", "28"],["100005", "6.6.6.1", "41"]],
                                    "ecmp-dst-member": "100005",
                                    "ecmp-dst-port": "41",
                                    "ecmp-next-hop-ip": "6.6.6.2"
                                },
                                {
                                    "ecmp-group-id": "200100",
                                    "ecmp-members": [["100001", "3.3.3.1", "31"],
["100002", "7.7.7.2", "21"]],
                                    "ecmp-dst-member": "100001",
                                    "ecmp-dst-port": "31",
                                    "ecmp-next-hop-ip": "3.3.3.2"
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
                                "lag-id": "3",
                                "lag-members": ["5","6","7","8"],
                                "dst-lag-member": "6",
                                "fabric-trunk-id": "6",
                                "fabric-trunk-members": ["27", "28", "29"],
                            }
                        },
                        {
                            "realm": "ecmp-link-resolution",
                            "data": [
                                {
                                    "ecmp-group-id": "200512",
                                    "ecmp-members": [["200004", "3.2.2.2", "38"],["100005", "6.6.6.1", "41"]],
                                    "ecmp-dst-member": "100010",
                                    "ecmp-dst-port": "19",
                                    "ecmp-next-hop-ip": "8.8.8.2"
                                },
                                {
                                    "ecmp-group-id": "200200",
                                    "ecmp-members": [["100002", "4.3.3.1", "76"], ["100002", "7.7.7.2", "21"]],
                                    "ecmp-dst-member": "100002",
                                    "ecmp-dst-port": "55",
                                    "ecmp-next-hop-ip": "7.3.3.2"
                                }
                            ]
                        }
                    ]
                }
            ],
            "id": 1
        }

def usage():
    print "pt_profile [-h host] [-p port]"

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

    x = PTProfile(host, port)
    x.send()
	
if __name__ == "__main__":
    main()	


