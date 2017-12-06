# [try to decrypt] Text 5 (middle) - Writeup

대략적인 패턴은 알았는데 코딩하기가 귀찮아서, 그냥 Blind SQL Injection처럼 짜서 돌려놓고 다른거 했다.

``` python
import urllib.parse, urllib.request

def query(data):
	url = 'https://www.trytodecrypt.com/decrypt.php?id=11'
	post_data = {
		'text':data,
		'encrypt':''
	}
	headers = {
		'Content-Type':'application/x-www-form-urlencoded'
	}
	req = urllib.request.Request(
		url, 
		urllib.parse.urlencode(post_data).encode(), 
		headers
	)
	res = urllib.request.urlopen(req).read().decode()
	ldelim = '                <div class="panel-body" style="word-wrap: break-word;">'
	rdelim = '</div>'
	res = res[res.find(ldelim)+len(ldelim):]
	res = res[:res.find(rdelim)]
	print(res)
	return res

def main():
	table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.,;:?! '

	encrypted = '3785824AD56B2531A7150DF44C21434A61E63F040A42F2012BC2F43F0AD535D24D46013213866D7E0'
	decrypted = ''

	for i in range(0, len(encrypted), 3):
		for k in table:
			x = encrypted[:i+3]
			temp = query(decrypted + k)
			if temp == x:
				decrypted += k
				print('find:', decrypted)
				break

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
You are very good. Respect!
```

___

## Answer

flag: `You are very good. Respect!`