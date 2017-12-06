# [try to decrypt] Text 6 (easy) - Writeup

``` python
def main():
	table1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.,;:?! '
	table2 = '038407080A8C0E1011941518189C1C201FA4232826AC2A302DB4313834BC38403BC43F4842CC465049D44D5850DC546057E45B685EEC627065F469786CFC7080740477887B0C7E9082148598891C8CA0902493A8972C9AB09E34A1B8A53CA8C0AC44AFC8B34CB6D0BA54BDD8C15CC4E0C864CBE8CF6CD2F0D674D9F8DD7CE100E484E808EB8CEF10F294F618F99C'
	table3 = dict()

	c = 0
	for i in range(0, len(table2), 4):
		y = table2[i:i+4]
		table3[y] = table1[c]
		c += 1

	encrypted = '4D586CFC2DB449D47B0CF99C3BC46CFC7B0C'
	decrypted = ''
	for i in range(0, len(encrypted), 4):
		x = encrypted[i:i+4]
		decrypted += table3[x]

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
lucky guy
```

___

## Answer

flag: `lucky guy`