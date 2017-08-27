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
sys.path.append('./gen-py')
sys.path.append('./dba')

from T2Redis import T2Redis
from T2Redis.ttypes import *

from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer

import redis_handler

class T2RedisHandler:
  def __init__(self):  
    self.log = {}
    self.redisclient = redis_handler.RedisHandler()
  def func1(self):  
    print 'func1()'  
  def initOK(self):  
    print 'sayHello'
    return 'OK'
  def saveData(self, key,value):
    self.redisclient.set(key,value)
    return ' from server 1024 __ ';

handler = T2RedisHandler()
processor = T2Redis.Processor(handler)
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
