# (C) Copyright 2016 PLUMgrid Inc.
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

from broadviewpublisherbase import BroadViewPublisherBase

# the Monasca serializer format is suitable for logging output,
# so use it.

from broadview_collector.serializers.bst_to_monasca import BSTToMonasca
from broadview_collector.serializers.pt_to_monasca import PTToMonasca
import json
import syslog

class BroadViewPublisher(BroadViewPublisherBase):

    def __init__(self):
        syslog.openlog(ident="BroadView")

    def __del__(self):
        syslog.closelog()

    def publish(self, host, data):
        code = 200
        if self.isBST(data):
            success, sdata = BSTToMonasca().serialize(host, data)
        elif self.isPT(data):
            success, sdata = PTToMonasca().serialize(host, data)
        else:
            success = False
        if success:
            sdata = json.loads(sdata)

            for x in sdata:
                syslog.syslog(json.dumps(x))
        else:
            code = 500
        return code

    def __repr__(self):
        return "BroadView syslog Publisher"

