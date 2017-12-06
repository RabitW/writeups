# [try to decrypt] Text 5 (easy) - Writeup

``` python
def main():
	table1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.,;:?! '
	table2 = '0C0F1215181B1E2124272A2D303336393C3F4245484B4E5154575A5D606366696C6F7275787B7E8184878A8D909396999C9FA2A5A8ABAEB1B4B7BABDC0C3C6C9CCCFD2D5D8DBDE'
	table3 = dict()

	c = 0
	for i in range(0, len(table2), 2):
		y = table2[i:i+2]
		table3[y] = table1[c]
		c += 1

	encrypted = '90DE633F425148DE51546CDE725466DE3F2A6936DE4263CCDEAB362A3372DE39545DDE633F36DE51366F63DE545136D8'
	decrypted = ''
	for i in range(0, len(encrypted), 2):
		x = encrypted[i:i+2]
		decrypted += table3[x]

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
I think now you have it. Ready for the next one?
```

___

## Answer

flag: `I think now you have it. Ready for the next one?`