#!/usr/bin/env python

#
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
sys.path.append('/Users/ke/workshop/flaskr/thrift/ptr/gen-py')
sys.path.append('/Users/ke/workshop/flaskr/thrift/ptr/redis')
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
    re =  self.redisclient.get('a')
    print re 
    return re+' from server 1024';
  

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

