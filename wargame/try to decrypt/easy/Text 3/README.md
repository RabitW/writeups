# [try to decrypt] Text 3 (easy) - Writeup

``` python
def main():
	table1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.,;:?! '
	table2 = 'F2F3F4F5F6F7F8F9FAFBFCFDFE000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F30313233343536373839'
	table3 = dict()

	c = 0
	for i in range(0, len(table2), 2):
		y = table2[i:i+2]
		table3[y] = table1[c]
		c += 1

	encrypted = '0A0B1339150B1139070A0B13390510'
	decrypted = ''
	for i in range(0, len(encrypted), 2):
		x = encrypted[i:i+2]
		decrypted += table3[x]

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
now you know it
```

___

## Answer

flag: `now you know it`