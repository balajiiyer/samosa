import fitbit
import json
import requests
import time

from samosa.utils.redis_utils import init_redis


def main():
    r = init_redis()
    while (1):
        for member in r.smembers('members'):
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
            time.sleep(1800)


if __name__ == "__main__":
    main()
