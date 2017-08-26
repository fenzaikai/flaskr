#!/usr/bin/env python

# Licensed to the Apache Software Foundation (ASF) under one  
# or more contributor license agreements. See the NOTICE file  
# distributed with this work for additional information  
# regarding copyright ownership. The ASF licenses this file  
# to you under the Apache License, Version 2.0 (the  
# "License"); you may not use this file except in compliance  
# with the License. You may obtain a copy of the License at  
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,  
# software distributed under the License is distributed on an  
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY  
# KIND, either express or implied. See the License for the  
# specific language governing permissions and limitations  
# under the License.
#
import sys, glob
sys.path.append('/Users/ke/workshop/flaskr/thrift/demo/gen-py')
sys.path.append('/Users/ke/workshop/flaskr/thrift/demo/redis')

from HelloService import HelloService
from HelloService.ttypes import *

from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer

import redis_handler

class HelloServiceHandler:
  def __init__(self):  
    self.log = {}
    self.redisclient = redis_handler.RedisHandler()
  def func1(self):  
    print 'func1()'  
  def sayHello(self):  
    print 'sayHello'  
  def getData(self, input):
    self.redisclient.set('a',input)
    return input+' from server 1024 __ ';

  # def getData(self, input):
  #   kv = input.split('_')

  #   
  #   r.set(key, value)

  #   if(len(kv) == 2):
  #     save2Redis(kv[0],kv[1]);
  #     print(kv[0]+"___"+kv[1]);
  #   else:
  #     print 'error'
  #   return r.get(key)

  # def save2Redis(key,value):
  #   r = redis.Redis(host='127.0.0.1', port=6379,db=0)
  #   r.set(key, value)

  # def getRedis(key):
  #   r = redis.Redis(host='127.0.0.1', port=6379,db=0)
  #   return r.get(key)


handler = HelloServiceHandler()
processor = HelloService.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()


server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# You could do one of these for a multithreaded server
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'
