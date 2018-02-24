import urllib.parse, urllib.request

def main():
	url = 'http://game.debu.kr/chall/750b2a79dda0dbf93b2779d071f21092/'
	headers = {
		'User-Agent':'debukuk_agent'
	}
	req = urllib.request.Request(url, None, headers)
	res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")

	print(res)

if __name__ == '__main__':
	main()