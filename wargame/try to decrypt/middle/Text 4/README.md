# [try to decrypt] Text 4 (middle) - Writeup

``` python
def main():
	table1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.,;:?! '
	table3 = dict()

	table2 = '10121413151716181A191B1D1C1E201F2123222426252729282A2C2B2D2F2E3032313335'
	c = 0
	f = 0
	for i in range(0, len(table2), 2):
		y = int(table2[i:i+2], 16) - f
		table3[y] = table1[c]
		c += 1
		f += 1
		if f == 3: f = 0

	table2 = '34363837393B3A3C3E3D3F4140424443454746484A494B4D4C4E504F51535254565557'
	c = 0
	f = 0
	for i in range(0, len(table2), 2):
		y = int(table2[i:i+2], 16) - f
		table3[y] = table1[c]
		c += 1
		f += 1
		if f == 3: f = 0

	encrypted = '261129152E152B'
	decrypted = ''
	f = 0
	for i in range(0, len(encrypted), 2):
		x = int(encrypted[i:i+2], 16) - f
		f += 1
		if f == 3: f = 0
		decrypted += table3.get(x, '?')

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
m0n5t3r
```

___

## Answer

flag: `m0n5t3r`