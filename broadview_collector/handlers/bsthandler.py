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

from broadviewhandlerbase import BroadViewHandlerBase
from broadview_lib.bst.bst_parser import BSTParser

class BroadViewHandler(BroadViewHandlerBase):
    def __init__(self):
        pass

    def handlePOST(self, path, ctype, length, data):
        parser = BSTParser()
        try:
            handled = parser.process(data)
        except:
            handled = False
        print handled
        return (parser, handled)

    def __repr__(self):
        return "BST Handler" 

