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

import fitbit
import json
import requests
import time

from samosa.utils.redis_utils import init_redis


def main():
    r = init_redis()
    while (1):
        for member in r.smembers('members'):
            print 'Collecting data for - ' + member
            person = r.hgetall(member)

            if person['device'] == "fitbit":
                creds = eval(person['credentials'])
                authd_client = fitbit.Fitbit(**creds)
                response = authd_client.activities()
                r.hmset(time.strftime("%d%m%Y") + member,
                        {"steps": response['summary']['steps']})
                r.hmset(time.strftime("%d%m%Y") + member,
                        {"caloriesBMR": response['summary']['caloriesBMR']})
                r.hmset(time.strftime("%d%m%Y") + member,
                        {"distances": response['summary']['distances'][0]['distance']})

            if person['device'] == "jawbone-up":
                http_url = 'https://jawbone.com/nudge/api/v.1.1/users/@me/moves'
                headers = eval(person['credentials'])
                headers['Accept-Header'] = "application/json"
                response = requests.get(http_url, headers=headers)
                resp_body = json.loads(response.content)

                r.hmset(time.strftime("%d%m%Y") + member,
                        {"steps": resp_body['data']['items'][0]['details']['steps'],
                         "caloriesBMR": resp_body['data']['items'][0]['details']['bmr'],
                         "distances": 1.6 * resp_body['data']['items'][0]['details']['km']})
        print 'Sleeping...'
        time.sleep(1800)


if __name__ == "__main__":
    main()
