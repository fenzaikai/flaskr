#!/usr/bin/python
# -*- coding:utf-8 -*-

import redis
import sys
import time
import numpy as np

class RedisHandler(object) :
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1',port=6379,db=0);
        self.timeInterval = []
    def set(self,k,v):
        begin = datetime.datetime.now()
        rs = self.r.set(k,v)
        end = datetime.datetime.now()
        self.timeInterval.append((end-begin).total_seconds())
        return rs
    def get(self,k):
        re = self.r.get(k);
        return re
    def mset(self):
        self.r.mset();


    def sayHello():
        str="hello"
        print(str);

a = RedisHandler()

print ('开始学习Redis')
for i in range(1, len(sys.argv)):
    term = sys.argv[i]
    print "[参数", i,"]",term
    if(term.find(",")>=0 and len(term.split(",")) == 2):
        key = term.split(",")[0]
        value = term.split(",")[1]
        if(key.find("key")>-1 and value.find("value")>-1):
            newkey = key[key.find(":")+1:]
            newvalue = value.replace("value:","")
            print "key:",newkey,"\nvalue:",newvalue
            for num in range(0,100):
                ret = a.set(newkey,newvalue)
            print "save to redis, return :",ret
            result = a.get(newkey)
            print "get result from redis, value :",result

    print "total_seconds:", np.array(a.timeInterval).sum()


print ('学习批处理函数')
a.timeInterval = []
print ('简单的for循环插入')
for num in range(0,100):
    key = num
    value = 'value is',num
#    print key," ",value
    ret = a.set(key,value)
print "total_seconds 1:", np.array(a.timeInterval).sum()

a.timeInterval = []
print ('使用pipeline插入')
begin = datetime.datetime.now()
p = a.r.pipeline()
for num in range(0,100):
    key = num
    value = 'value is',num
#    print key," ",value
    ret = p.set(key,value)
p.execute()
end = datetime.datetime.now()
a.timeInterval.append((end-begin).total_seconds())
print "total_seconds 2:", np.array(a.timeInterval).sum()
