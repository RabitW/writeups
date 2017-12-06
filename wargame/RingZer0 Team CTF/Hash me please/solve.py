import urllib
import httplib
import hashlib

HTTP=httplib.HTTPSConnection("ringzer0team.com")
Param=urllib.urlencode({})
Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
HTTP.request("GET","/challenges/13",Param,Headers)
Result=HTTP.getresponse().read()

Buffer1=Result.split("----- BEGIN MESSAGE -----<br />\r\n		")
Buffer2=Buffer1[1].split("<br />")
hashval=hashlib.sha512(Buffer2[0]).hexdigest()

HTTP=httplib.HTTPSConnection("ringzer0team.com")
Param=urllib.urlencode({})
Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
HTTP.request("GET","/challenges/13/"+hashval,Param,Headers)
Result=HTTP.getresponse().read()
Result2=Result.split("<div class=\"challenge-wrapper\">\r\n		")
Result3=Result2[1].split("\">")
Result4=Result3[1].split("</div>")
print Result4[0]
