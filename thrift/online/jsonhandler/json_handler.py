import json

class JsonHandler(object):

    def __init__(self):
          pass
    #输入{String a} 返回{String}，例子：输入：yingyu:30, shuxue:85 返回：对应的json；
    def genJson(self,str):
        // 按照，分隔字符串，再按照：取key，value
        a = str.split(',')
        data = '{'
        for x in a:
            b = x.split(':')
            data += '"'+b[0]+'":"'+b[1]+'",'
        data = data[:-1]
        data += '}'
        re = json.dumps(data)
        return re

    #输入{String json, String key}，例子：输入{Json, yingyu} 返回:30
    def getAttrs(self,json,key):
        a = json.loads(json)
        data = a[1:-1]
        data = data.split(',')
        re = 0
        for y in data:
            z = y.split(':')
            zz = z[0].rstrip('"')
            if(key == zz):
                re = z[1].rstrip['"']
        return re
