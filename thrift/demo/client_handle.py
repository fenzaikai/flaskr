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

sys.path.append('/Users/ke/workshop/flaskr/thrift/demo/gen-py')
  
from HelloService import HelloService  
from HelloService.ttypes import *  
  
  
from thrift import Thrift  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol

class clientHandler(object):
    def __init__(self):
        self.transport = TSocket.TSocket('localhost', 9090)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = HelloService.Client(self.protocol)
        self.transport.open()
    def close(self):
      self.transport.close()
    def sayHello(self):
      self.client.sayHello();
      print 'ping()'

    def getData(self,a):
      print(self.client.getData("client_access"))
