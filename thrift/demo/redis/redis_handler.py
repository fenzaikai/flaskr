import redis

class RedisHandler(object):
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379,db=0);
    def set(self,k,v):
        self.r.set(k,v)
