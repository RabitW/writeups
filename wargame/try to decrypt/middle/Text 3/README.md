# [try to decrypt] Text 3 (middle) - Writeup

``` python
def reverse(data):
	res = ''
	for i in range(0, len(data), 3):
		y = data[i:i+3]
		res = y + res
	return res

def main():
	table1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.,;:?! '
	table2 = reverse('6684382080D7E97C67A378076D64A6276046E06CD5AA58756454152E40B4E74C44A148E36B3483253023EE2CB2A828526224F12C1091')
	table2 += reverse('C3FA0F8DE6AE47E24E01EEDDCADA7D84D61D4EC2BC08CE4CC1CAEB8BB68B45B22B0FAEBAC8AA5A82A6F94C9299069E29CF8AC8898')
	table3 = dict()

	c = 0
	for i in range(0, len(table2), 3):
		y = table2[i:i+2]
		table3[y] = table1[c]
		c += 1

	encrypted = reverse('6224F12C1C3FAA5AA54836B3C446D6415E74')
	decrypted = ''
	for i in range(0, len(encrypted), 3):
		x = encrypted[i:i+2]
		decrypted += table3[x]

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
fireball 123
```

___

## Answer

flag: `fireball 123`