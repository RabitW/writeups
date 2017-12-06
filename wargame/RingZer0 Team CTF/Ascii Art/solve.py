import urllib
import httplib

HTTP=httplib.HTTPSConnection("ringzer0team.com")
Param=urllib.urlencode({})
Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
HTTP.request("GET","/challenges/119",Param,Headers)
Result=HTTP.getresponse().read()

Buffer1=Result.split("----- BEGIN MESSAGE -----<br />\r\n		")
Buffer2=Buffer1[1].split("<br />\r\n		----- END MESSAGE -----")
temp=Buffer2[0].replace("&nbsp;"," ")
temp=temp.replace("<br />","\n")


temp=temp.replace(" xxx \nx   x\nx   x\nx   x\n xxx \n","0")
temp=temp.replace(" xx  \nx x  \n  x  \n  x  \nxxxxx\n","1")
temp=temp.replace(" xxx \nx   x \n  xx \n x   \nxxxxx\n","2")
temp=temp.replace(" x   x\nx    x\n xxxxx\n     x\n    x\n","4")
temp=temp.replace(" xxx \nx   x\n  xx \nx   x\n xxx \n","8")
temp=temp.replace("xxxxx\nx    \n xxxx\n    x\nxxxxx\n","5")
temp=temp.replace("\n","")
print temp

HTTP=httplib.HTTPSConnection("ringzer0team.com")
Param=urllib.urlencode({})
Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
HTTP.request("GET","/challenges/119/"+temp,Param,Headers)
Result=HTTP.getresponse().read()
Result2=Result.split("<div class=\"challenge-wrapper\">\r\n		"
)
Result3=Result2[1].split("\">"
)
Result4=Result3[1].split("</div>")
print Result4[0]
