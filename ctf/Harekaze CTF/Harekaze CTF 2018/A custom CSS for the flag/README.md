# A custom CSS for the flag

1. CSS의 `@font-face`와 `unicode-range`를 이용하면, `unicode-range`에 설정된 범위의 문자열이 HTML 문서 내에 존재할 경우 해당 폰트 페이지에 접속을 요청하므로, 그걸 이용해서 flag를 구성하는 문자열을 유추할 수 있다.
	따라서 [css.php](./localhost/css.php)를 내 서버에 넣어두고, 해당 URL을 입력하면 해당 CSS 파일을 문제 서버의 Chromium 엔진에서 임포트할 것이다.

2. 그리고 [log.php](./localhost/log.php)에 의해 접속된 [로그](./localhost/logs/)를 살펴보면, `163.43.29.129` 아이피로부터 접속된 로그에 flag를 구성하는 문자열인 `-{HFCzrokebatmlf_usni}Tdc`이 로깅되어있다.

3. 본 문제의 설명에 flag는 CSS3 속성 2개를 언더스코어(`_`)로 이어붙인 문자열이라고 나와있다.
	그러므로 CSS3 속성 테이블([css3_property_table.txt](css3_property_table.txt))을 만들어두고 매치시켜보면, flag로 예상되는 문자열들을 유효한 범위 내로 구할 수 있다.
	이 부분은 손수 하기엔 시간이 오래 걸리므로 [자동화 스크립트](./get_flag_from_css3_table/)를 작성하여 돌렸다.

4. flag는 `HarekazeCTF{border-bottom-left-radius_animation-direction}`이다.
