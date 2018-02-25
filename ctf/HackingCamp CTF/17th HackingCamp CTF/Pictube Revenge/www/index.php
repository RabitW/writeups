<?php
	$filepath = __DIR__."/log/".$_SERVER['REMOTE_ADDR'].".txt";
	$filebody = urldecode($_SERVER['QUERY_STRING'])."\r\n\r\n";
	file_put_contents($filepath, $filebody, FILE_APPEND);
?>