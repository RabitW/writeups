import urllib
import httplib
import hashlib

HTTP=httplib.HTTPSConnection("ringzer0team.com")
Param=urllib.urlencode({})
Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
HTTP.request("GET","/challenges/57",Param,Headers)
Result=HTTP.getresponse().read()

Buffer1=Result.split("----- BEGIN HASH -----<br />\r\n		")
Buffer2=Buffer1[1].split("<br />")
hashval=Buffer2[0]

Buffer1=Result.split("----- BEGIN SALT -----<br />\r\n		")
Buffer2=Buffer1[1].split("<br />")
saltval=Buffer2[0]

plaintext=""
for i in range(1000,9999):
        if str(hashlib.sha1(str(i)+saltval).hexdigest()) == hashval:
                plaintext=str(i)
                break

HTTP=httplib.HTTPSConnection("ringzer0team.com")
Param=urllib.urlencode({})
Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
HTTP.request("GET","/challenges/57/"+plaintext,Param,Headers)
Result=HTTP.getresponse().read()
Result2=Result.split("<div class=\"challenge-wrapper\">\r\n		")
Result3=Result2[1].split("\">")
Result4=Result3[1].split("</div>")
print Result4[0]
