<?php
# http://misc.peng.kr/log.php
	if(isset($_SERVER['QUERY_STRING']{0})){
		file_put_contents(
			__DIR__."/logs/".$_SERVER['REMOTE_ADDR'].".txt",
			urldecode($_SERVER['QUERY_STRING']),
			FILE_APPEND
		);
	}
?>