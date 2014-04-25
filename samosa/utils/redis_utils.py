import redis


def init_redis():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    return r