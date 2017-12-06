# [try to decrypt] Text 1 (easy) - Writeup

``` python
def main():
	table1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.,;:?! '
	table2 = '02030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F303132333435363738393A3B3C3D3E3F404142434445464748'
	table3 = dict()

	c = 0
	for i in range(0, len(table2), 2):
		y = table2[i:i+2]
		table3[y] = table1[c]
		c += 1

	encrypted = '131017171A48221A1D170F'
	decrypted = ''
	for i in range(0, len(encrypted), 2):
		x = encrypted[i:i+2]
		decrypted += table3[x]

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
hello world
```

___

## Answer

flag: `hello world`