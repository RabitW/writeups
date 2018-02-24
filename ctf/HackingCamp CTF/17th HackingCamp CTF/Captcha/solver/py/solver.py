import urllib.parse, urllib.request
import base64
from PIL import Image
import os
import time

c=0

def check(answer):
	global c
	url = 'http://debu.kr:53201/8671d960384a6dc7410701db14af4db2/'
	params = {
		'answer': answer
	}
	headers = {
		'User-Agent':'Mozilla/5.0',
		'Cookie':'CAPTCHA_GAME=7ppscj4irl9ae3dmgidskv1io0' + str(c)
	}
	req = urllib.request.Request(url, urllib.parse.urlencode(params).encode(), headers)
	res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
	print(res)
	return "Correct" in res

def main():
	global c
	while True:
		url = 'http://debu.kr:53201/8671d960384a6dc7410701db14af4db2/'
		headers = {
			'User-Agent':'Mozilla/5.0',
			'Cookie':'CAPTCHA_GAME=7ppscj4irl9ae3dmgidskv1io0' + str(c)
		}
		req = urllib.request.Request(url, None, headers)
		res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
		print(res)
		b64 = res
		b64 = b64[b64.find("data:image/png;base64,")+len("data:image/png;base64,"):]
		b64 = b64[:b64.find("'>")]
		imgbin = base64.b64decode(b64)

		f=open("temp.png", "wb")
		f.write(imgbin)
		f.close()

		img=Image.open("temp.png")
		pixels=img.load()
		img.save("temp.bmp")

		os.system("temp.exe")

		f=open("temp.txt", "rb")
		answer = f.read().decode()
		f.close()

		print('7ppscj4irl9ae3dmgidskv1io0' + str(c) + " : " + answer)
		if check(answer):
			print("Correct")
			pass
		else:
			c += 1
			print(answer)


if __name__ == '__main__':
	main()