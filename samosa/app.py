#!/usr/bin/env python

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#   Copyright 2014 Balaji Iyer, Sriram Vasudevan

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

        sorted_resp = sorted(resp_return, key=lambda k: k['data']['steps'], reverse=True)
        resp.status = falcon.HTTP_200
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.body = json.dumps(sorted_resp)



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
