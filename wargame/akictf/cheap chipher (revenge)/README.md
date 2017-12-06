# [akictf] cheap chipher (revenge) - Writeup

``` python
import base64

encoded = "rKrUl+/clKHb4u/sm6sgnaPfnO/XkO=ewqPU45bRjp4gwa7NntoM467Onu/enqPRlakgj6Egjp0e1gAA"
decoded = ["?"] * len(encoded)

table_a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
table_b = table_a[::-1]

for i in range(len(encoded)):
	for k in range(len(table_a)):
		if encoded[i] == table_a[k]:
			decoded[i] = table_b[k]

decoded = base64.b64decode("".join(decoded)).decode()
print(decoded)
```
```
Well done! The flag is "All your Base64 are belong to us".
```

___

## Answer

flag: `All your Base64 are belong to us`