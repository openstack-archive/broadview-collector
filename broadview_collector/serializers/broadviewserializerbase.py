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

class BroadViewSerializerBase(object):
    def __init__(self):
        pass

    def serialize(self, data):
        '''
        return a 2-tuple (ret, jsonret)

        where coderet is True for success and False for failure,
        jsonret is a json string that holds the serialized data.

        For example, on success:

        return (True, "{\"foo\": \"bar\"}")
        '''

        raise NotImplementedError
