<?php

	$table = "28252F1216EEFC04F1020BF01406EC03FD000710F6F70807B4F6EEF3";
	$table = hex2bin($table);

	$ans = "php_file_is_so_beautiful.php";

	for($i = 0; $i < strlen($table); ++$i){
		$ok = "?";
		for($k = 0; $k < 512; ++$k){
			if(chr(ord($table[$i]) + $k) == $ans[$i]){
				$ok = chr($k);
				break;
			}
		}
		echo $ok;

	}
