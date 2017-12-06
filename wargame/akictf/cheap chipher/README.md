# [akictf] cheap chipher - Writeup

문자열을 뒤집은 후, base64로 인코딩하고, 다시 뒤집은 형태로 되어있다.

``` python
import base64

print(base64.b64decode("==AVoVGImxWYnBSazByUzMkUzQ1XLNTW".encode()[::-1])[::-1].decode())
```
```
The flag is S3CR3T_K3Y
```

___

## Answer

flag: `S3CR3T_K3Y`