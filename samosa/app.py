
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

import falcon
import json
import redis

from samosa.utils.json_utils import read_json


class UserStatsResource:
    def on_get(self, req, resp):
        pass


class UserRegisterResource:
    def on_post(self, req, resp):
        document = read_json(req.stream, req.content_length)
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        r.sadd('members', document['name'])
        r.hmset(document['name'], dict((k, v) for k, v in document.items() if k not in 'name'))
        resp.status = falcon.HTTP_200
        resp.body = "Success"

app = falcon.API()

user_stats = UserStatsResource()
register_samosa = UserRegisterResource()

app.add_route('/stats', user_stats)
app.add_route('/user', register_samosa)
