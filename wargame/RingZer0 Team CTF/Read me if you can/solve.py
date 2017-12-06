import urllib
import httplib
import hashlib
import base64
import Image
import subprocess, os
import time

 
HTTP=httplib.HTTPSConnection("ringzer0team.com")
Param=urllib.urlencode({})
Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
HTTP.request("GET","/challenges/17",Param,Headers)
Result=HTTP.getresponse().read()

Buffer1=Result.split("<img src=\"data:image/png;base64,")
Buffer2=Buffer1[1].split("\" />")

d=base64.b64decode(Buffer2[0])
e=open("temp.png","wb")
e.write(d)
e.close()

img=Image.open("temp.png")
pixels=img.load()
(x,y)=img.size
for j in range(0,y,1):
    for i in range(0,x,1):
        rgb=pixels[i,j]
        
        if rgb[0] == 0xff & rgb[1] == 0xff & rgb[2] == 0xff:
            pixels[i,j] = (0, 0, 0)
        else:
            pixels[i,j] = (255, 255, 255)
#img.show()
img.save("temp.bmp")

PIPE=subprocess.PIPE
p=subprocess.Popen("temp.exe", stdin=PIPE, stdout=PIPE)
time.sleep(0.5)

e=open("temp.txt","r")
origintext=e.read()
e.close()

print origintext

HTTP=httplib.HTTPSConnection("ringzer0team.com")
Param=urllib.urlencode({})
Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
HTTP.request("GET","/challenges/17/"+origintext,Param,Headers)
Result=HTTP.getresponse().read()
Result2=Result.split("<div class=\"challenge-wrapper\">\r\n		"
)
Result3=Result2[1].split("\">"
)
Result4=Result3[1].split("</div>")
print Result4[0]
