import urllib
import httplib
import hashlib

def checkweb():
    HTTP=httplib.HTTPSConnection("ringzer0team.com")
    Param=urllib.urlencode({})
    Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
    HTTP.request("GET","/challenges/159",Param,Headers)
    Result=HTTP.getresponse().read()

    Buffer1=Result.split("----- BEGIN HASH -----<br />\r\n		")
    Buffer2=Buffer1[1].split("<br />")

    if Buffer2[0] in a:
        print "ok -- "+str(a[Buffer2[0]])
    else:
        print "fail"
        checkweb()

    HTTP=httplib.HTTPSConnection("ringzer0team.com")
    Param=urllib.urlencode({})
    Headers={"Cookie":"PHPSESSID=ch779ru3qvb5fdc9jm2cnmt752;"}
    HTTP.request("GET","/challenges/159/"+str(a[Buffer2[0]]),Param,Headers)
    Result=HTTP.getresponse().read()
    Result2=Result.split("<div class=\"challenge-wrapper\">\r\n		"
    )
    Result3=Result2[1].split("\">"
    )
    Result4=Result3[1].split("</div>")
    print Result4[0]



a={"":0}
plaintext=""
temp=""
for z in range(97,122):
    for x in range(97,122):
        for c in range(97,122):
            for v in range(97,122):
                for b in range(97,122):
                    for n in range(97,122):
                        plaintext=str(chr(z)+chr(x)+chr(c)+chr(v)+chr(b)+chr(n))
                        temp=str(hashlib.sha1(plaintext).hexdigest())
                        temp=temp[:6]
                        a[temp]=plaintext
        print chr(z)+chr(x)+"aaaa ~ "+chr(z)+chr(x)+"zzzz -- OK"

checkweb()

