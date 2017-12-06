# [akictf] easy crackme - Writeup

ELF 바이너리 분석 문제인데, flag는 그냥 바로 찾을 수 있었다.

하지만 flag가 ASCII가 아닌 약간 이상한 문자들로 이루어져 있어서, 쉽게 auth되지 않는다.

``` python
import urllib.parse, urllib.request

def main():
	url = 'https://ctf.katsudon.org/answer'
	post_data = {
		'problem_id':'10',
		'flag':b'\xE6\x97\x97\x52\x4D\x37\x52\x46\x34\x6F\x32',
		'csrf_token':'**secret**'
	}
	headers = {
		'Cookie':'akictf_session=**secret**',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'X-Requested-With':'XMLHttpRequest'
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

___

## Answer

flag: `\xE6\x97\x97\x52\x4D\x37\x52\x46\x34\x6F\x32`