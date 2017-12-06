# [try to decrypt] Text 4 (easy) - Writeup

``` python
def main():
	table1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.,;:?! '
	table2 = '1E1D1C1B1A191817161514131211100F0E0D0C0B0A09080706050403020100FFFEFDFCFBFAF9F8F7F6F5F4F3F2F1F0EFEEEDECEBEAE9E8E7E6E5E4E3E2E1E0DFDEDDDCDBDAD9D8'
	table3 = dict()

	c = 0
	for i in range(0, len(table2), 2):
		y = table2[i:i+2]
		table3[y] = table1[c]
		c += 1

	encrypted = '0C02D8010D0C02D8010606D8101402FCD80F0603D8FC0600DA'
	decrypted = ''
	for i in range(0, len(encrypted), 2):
		x = encrypted[i:i+2]
		decrypted += table3[x]

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
is this too easy for you?
```

___

## Answer

flag: `is this too easy for you?`