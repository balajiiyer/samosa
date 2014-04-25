
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
import time

from samosa.utils.json_utils import read_json
from samosa.utils.redis_utils import init_redis

class UserStatsResource:
    def on_get(self, req, resp):
        pass


class LeaderboardResource:
    def on_get(self, req, resp):
        r = init_redis()
        resp_return = []
        for member in r.smembers('members'):
            details = r.hgetall(time.strftime("%d%m%Y")+member)
            resp_return.append({"user": member, "data": details})
        resp.status = falcon.HTTP_200
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.body = json.dumps(resp_return)



class UserRegisterResource:
    def on_post(self, req, resp):
        document = read_json(req.stream, req.content_length)
        r = init_redis()
        r.sadd('members', document['name'])
        r.hmset(document['name'], dict((k, v) for k, v in document.items() if k not in 'name'))
        resp.status = falcon.HTTP_200
        resp.body = "Success"

app = falcon.API()

user_stats = UserStatsResource()
register_samosa = UserRegisterResource()
leaderboard = LeaderboardResource()

app.add_route('/stats', user_stats)
app.add_route('/leaderboard', leaderboard)
app.add_route('/user', register_samosa)
