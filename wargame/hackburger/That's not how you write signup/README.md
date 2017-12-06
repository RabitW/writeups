# [hackburger] That's not how you write signup - Writeup

## SQL Injection

주석에 의하면 `username`은 `varchar(25)`로 되어있기 때문에, 가입 시에 25글자 이상으로 값을 넣으면 DB에 저장될때는 25글자까지만 저장된다.

따라서 `username`을 `admin\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20ㅁㄴㅇㄹ`으로 가입하고, `admin`으로 로그인하면 된다.

___

## Answer

flag: `ad0f46b77ae29d84a5f2b3a9b0784853d2aee093`