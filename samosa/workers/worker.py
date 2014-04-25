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
                cleaned_creds = dict((str(k), str(v)) for k, v in creds.items())
                authd_client = fitbit.Fitbit(
                    client_key=cleaned_creds['client_key'],
                    client_secret=cleaned_creds['client_secret'],
                    resource_owner_key=cleaned_creds['resource_owner_key'],
                    resource_owner_secret=cleaned_creds['resource_owner_secret'])
                response = authd_client.activities()
                r.hmset(
                    time.strftime("%d%m%Y") +
                    member,
                    dict(
                        (k,
                         v) for k,
                        v in response.items() if k in [
                            'steps',
                            'caloriesBMR']))
                r.hmset(time.strftime("%d%m%Y") + member,
                        {"distances": response['distances'][0]['distance']})
            if person['device'] == "jawbone-up":
                # http_url = 'https://jawbone.com/nudge/api/v.1.1/users/@me/moves?date=' + time.strftime("%d%m%Y")
                http_url = 'https://jawbone.com/nudge/api/v.1.1/users/@me/moves'
                headers = eval(person['credentials'])
                headers['Accept-Header'] = "application/json"
                response = requests.get(http_url, headers=headers)
                resp_body = json.loads(response.content)
                r.hmset(time.strftime("%d%m%Y") + member,
                        {"steps": resp_body['data']['items'][0]['details']['km'],
                         "caloriesBMR": resp_body['data']['items'][0]['details']['bmr'],
                         "distances": 1.6 * resp_body['data']['items'][0]['details']['bmr']})
        time.sleep(1800)


if __name__ == "__main__":
    main()
