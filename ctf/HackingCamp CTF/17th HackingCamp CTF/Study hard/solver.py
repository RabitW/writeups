import urllib.parse, urllib.request


def main():
	answer = ""
	for i in range(100):
		url = 'http://debu.kr:53201/7e1f721e6d50e4f2122f3145d7346156/'
		headers = {
			'User-Agent':'Mozilla/5.0',
			'Cookie':'STUDY_HARD=5f97285sbugoeptq1csuj4hrb6'
		}
		req = urllib.request.Request(url, None, headers)
		res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")

		print(res)

		if 0:
			pass
		elif " ;ls -al;echo 123" in res:
			answer = "command injection"

		elif "그 중에서 웹해킹을 하는 사람을 뭐라고 하는가?" in res:
			answer = "web hacker"

		elif "고급 언어, 범용 언어, 인터프리터 언어, 동적 언어 범주에 속한다. 이 계열의 언어에는 ???? 5와 ???" in res:
			answer = "Perl"

		elif " 객체 기반의 스크립트 프로그래밍 언어이다." in res:
			answer = "javascript"

		elif "'Quick Response'에서 유래하였다." in res:
			answer = "qr code"

		elif "echo 1 ? 'Y' : 'N';" in res:
			answer = "Y"

		elif "php에는 현재 사용하고 있는 php 정보들을 확인할 수 있는 함수가 존재한다." in res:
			answer = "phpinfo"

		elif "print(5 ^ 3)" in res:
			answer = "6"

		elif "메모리를 다루는 데에 오류가 발생하여 잘못된 " in res:
			answer = "buffer overflow"
			
		elif "ayer , Data link layer , Netwo" in res:
			answer = "Physical"
			
		elif "해킹은 영어로 무엇인" in res:
			answer = "hacking"
			
		elif "세계에서 가장 많이 쓰이는 오픈 소스의 관계형 데이터베이스 관리 시스템(RDBMS" in res:
			answer = "mysql"
			
		elif "Hello ?????" in res:
			answer = "world"
			
		elif "해킹에는 여러가지 분야가 존재한다. 그 중에서 리버스 엔지니어링을 하는 사람을 뭐라고 하는가?<" in res:
			answer = "reverser"
			
		elif "Hello ?????" in res:
			answer = "world"
			
		elif " WWW 상에서 정보를 주고받을 수 있는 프로토콜이다. 주" in res:
			answer = "http"
			
		elif "debu.kr의 아이피는" in res:
			answer = "45.77.40.158"
			
		elif "Hello ?????" in res:
			answer = "world"
			
		elif "991년 프로그래머인 귀도 반 로섬(Guido van Ro" in res:
			answer = "python"
			
		elif "HTTP 상태 코드에서 메시지가 Not Found 코드번호는" in res:
			answer = "404"
			
		elif "연속되지 않는 공간을 다룬다. 유한수학이라고도 하며, 전산" in res:
			answer = "Discrete mathematics"
			
		elif " 웹 페이지를 위한 지배적인 마크업 언어다." in res:
			answer = "html"
			
		elif "응용 프로그램 보안 상의 허점을 의도적으로 이용해, 악의적인 SQL문을 실행되" in res:
			answer = "sql injection"
			
		elif "사람들은 아래의 공격코드를 뭐라고 칭하여 부르는가?" in res:
			answer = "shell code"
			
		elif "퓨터에 악영향을 끼칠 수 있는 모든 소프트웨어의 총칭이다." in res:
			answer = "malware"
			
		elif "무결성의 영어 스펠링을 입력하시오." in res:
			answer = "integrity"
			
		elif "를 글자 그대로 번역하여 보면 64진법이란 뜻이다. 특별히 64진법이 컴퓨터에서 흥미" in res:
			answer = "base 64"
			
		elif "???????는 BSD 계열의 오픈 소스 운영 체제로서, 캘리포니아 대학" in res:
			answer = "FreeBSD"
			
		elif "????? ????? 프로그램은 \"?????, ?????!\"를 화면에 출력하는 컴퓨" in res:
			answer = "hello world"
			
		elif "HTTP 상태 코드에서 메시지가 Internal Server Error인 코드번호는?" in res:
			answer = "500"
			
		elif "?????????이라는 단어는 페르시아의 수학자이던 알콰리즈미의 이름에서 따온 것이다. " in res:
			answer = "algorithm"
			
		elif " 소프트웨어 혹은 하드웨어의 제작자의 권리를 지키면서 원시 코드를 누구나 열람할 수 있도록 한 소프트웨어 혹은" in res:
			answer = "open source"

		elif "Example) ' or 1#</pre>" in res:
			answer = "sql injection"

		elif "가용성의 영어 스펠링을 입력하시오" in res:
			answer = "Availability"

		elif "Example) ' or 1#</pre>" in res:
			answer = "sql injection"

		elif " 웹 애플리케이션에서 많이 나타나는 취약점의 하나로 웹사이트 관리자가" in res:
			answer = "xss"

		elif "print(1 + 1)" in res:
			answer = "2"

		elif " 해커스쿨이 공동으로 진행하는 해킹·보안 캠프입니다." in res:
			answer = "hackingcamp"

		elif "print(1 + 1)" in res:
			answer = "2"

		elif "print('hackcamp'.replace('hack', 'hacking'))" in res:
			answer = "hackingcamp"

		elif "그러나 이 방법으로는 많은 정보를 담기 어렵기 때문에 매트릭스(2차원) 코" in res:
			answer = "barcode"

		elif "Data link layer , ??????? layer , Transport layer , S" in res:
			answer = "network"

		elif "기밀성의 영어 스펠링을 입력하시오." in res:
			answer = "Confidentiality"

		elif "hackingcamp.org의 아이피는" in res:
			answer = "49.236.146.115"

		elif "HTTP 상태 코드에서 메시지가 OK인 코드번호는?" in res:
			answer = "200"

		elif "HTTP 상태 코드에서 메시지가 Request-URI too long 코드번호는?" in res:
			answer = "414"

		elif " 프로그래밍 언어의 일종이다. 원래는 동적 웹 페이지를 만들기 위해 설계되었으며" in res:
			answer = "php"

		elif "World Wide Web은 인터넷에 연결된 컴퓨터들을 통해 사" in res:
			answer = "www"

		elif "print(1 + 1)" in res:
			answer = "2"

		elif "보안의 3요소는 <기밀성, 무결성, 가용성> 이렇게 세가지가" in res:
			answer = "CIA"

		elif "NU ????(대개 ????)은 GNU 프로젝트의 부트로더이다" in res:
			answer = "GRUB"

		elif "보안은 영어로 무엇인가?" in res:
			answer = "security"

		elif "CTF(Capture The ????)에서는 문제의 정답을 ????라고 한다." in res:
			answer = "flag"

		elif "????????는 보안 전문 업체 소프트포럼에서 매년 주최하는 국제보안콘퍼런스, 국제해킹방어대회" in res:
			answer = "codegate"

		elif "CTF(Capture The ????)에서는 문제의 정답을 ????라고 한다." in res:
			answer = "flag"

		elif "echo 1 ? 'Y' : 'N';" in res:
			answer = "Y"

		elif "$a=&quot;debukuk&quot;;" in res:
			answer = "i am debukuk"

		elif "Capture The Flag의 이니셜은?</pre><" in res:
			answer = "ctf"

		elif "n+=123" in res:
			answer = str(123*5)

		elif " ');phpinfo();</" in res:
			answer = "code injection"

		elif "hello&quot;, &quot;world" in res:
			answer = "helloworld"

		elif "echo 0 ? 'Y' : 'N';" in res:
			answer = "N"

		elif "보통은 ???라고 부르는 GNU 디버거(GNU Debugger)" in res:
			answer = "gdb"

		elif "체계화된 데이터의 모임이다. 즉, 작성된 목록으로써 " in res:
			answer = "database"

		elif "세계 최대의 컴퓨터 보안 컨퍼런스이자 해킹 대회이다." in res:
			answer = "defcon"

		else:
			break

		url = 'http://debu.kr:53201/7e1f721e6d50e4f2122f3145d7346156/'
		params = {
			'answer':answer
		}
		headers = {
			'User-Agent':'Mozilla/5.0',
			'Cookie':'STUDY_HARD=5f97285sbugoeptq1csuj4hrb6'
		}
		req = urllib.request.Request(url, urllib.parse.urlencode(params).encode(), headers)
		res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")


if __name__ == '__main__':
	main()