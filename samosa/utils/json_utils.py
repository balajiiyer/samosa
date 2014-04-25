
# Copyright 2014 Balaji Iyer, Sriram Vasudevan
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json


class MalformedJSON(ValueError):
    """JSON string is not valid."""
    pass


def read_json(stream, content_length):
    try:
        return json.loads(stream.read(content_length))

    except ValueError as ex:
        raise MalformedJSON(ex)
