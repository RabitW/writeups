# [try to decrypt] Text 6 (middle) - Writeup

``` python
import urllib.parse, urllib.request

def query(data):
	url = 'https://www.trytodecrypt.com/decrypt.php?id=12'
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
	table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.,;:?! '

	encrypted = '00D02703603C0450461340870A50B50EA10A0BD133'
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
cookie monster
```

___

## Answer

flag: `cookie monster`