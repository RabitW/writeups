import sys
import threading
import urllib.parse
import urllib.request


def query(number):
	url = 'http://dimitrust.oa.to:8080/trustctf/lucky_number/?number=' + str(number)
	headers = {
		'User-Agent':'Mozilla/5.0'
	}
	req = urllib.request.Request(url, None, headers)
	res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")

	if "Try more!" not in res:
		print(res)


def main():
	for i in range(10000):
		threading.Thread(target = query, args = (i, )).start()


if __name__ == '__main__':
	main()