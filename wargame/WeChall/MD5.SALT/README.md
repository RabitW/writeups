# [WeChall] MD5.SALT - Writeup

`admin`으로 로그인해야하는 문제다.

___

## 1. SQL Injection

`username`에 SQLi를 시도해봤다.

`'||username='admin`를 넣어본 결과, SQLi는 되는데 패스워드를 따로 체크하는지 클리어는 안된다.

패스워드를 얻어야하는 문제 같다.

___

## 2. Union Based SQL Injection

패스워드를 얻기 위해 Union Based SQL Injection를 시도해봤다.

`'union select password,2 from users where username='admin`를 넣어본 결과, `215c61d0104f8925b5f7e4e87a7cbdfa` 라는 MD5 해시된 패스워드를 얻을 수 있었다.

___

## 3. Hash Crack

MD5 Online ([http://www.md5online.org/](http://www.md5online.org/))을 통해 위 해시를 크랙할 수 있었다.

크랙한 결과, 원문은 `academicsalt21` 이었다.

___

## 4. Salt Guess

`admin` / `academicsalt21` 로 로그인을 시도해봤는데 안된다.

문제 이름을 보아하니 해시 솔트가 있는 것 같다.

`salt21` 가 솔트임을 추측하고,  `admin` / `academic` 으로 로그인을 시도해봤더니 풀렸다.