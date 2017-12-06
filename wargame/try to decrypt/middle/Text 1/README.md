# [try to decrypt] Text 1 (middle) - Writeup

``` python
def main():
	table1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.,;:?! '
	table2 = '2A1B43172B012E093339270B41450E1011052F1C161804353E371D1F15211A23000C3B301E13253C292C31220D0F34383A3D02082D362432200A063F1914402603420744284612'
	table3 = dict()

	c = 0
	for i in range(0, len(table2), 2):
		y = table2[i:i+2]
		table3[y] = table1[c]
		c += 1

	encrypted = '21052F151200271512413E35101A152F3511'
	decrypted = ''
	for i in range(0, len(encrypted), 2):
		x = encrypted[i:i+2]
		decrypted += table3[x]

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
this was confusing
```

___

## Answer

flag: `this was confusing`