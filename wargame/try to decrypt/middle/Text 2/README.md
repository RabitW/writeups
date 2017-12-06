# [try to decrypt] Text 2 (middle) - Writeup

``` python
def main():
	table1 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.,;:?! '
	table2 = 'akmanhbacbcnbfibidbkobnjcaeccpcfkcifclacnldagddbdfmdihdlcdnneaieddefoeijeleenpfakfdffgafilflgfobgamgdhggcgingligodhaohdjhgehiphlkhofibaidliggijbilmiohjbcjdnjgijjdjlojojkbekdpkgkkjfkmakollbgleblgmljhlmclonmbimedmgo'
	table3 = dict()

	c = 0
	for i in range(0, len(table2), 3):
		y = table2[i:i+3]
		table3[y] = table1[c]
		c += 1

	encrypted = 'eaidagdagenpmgodlceijmgoefodlceijcnllonmgodlcfilfgamgodnnflgfgafilmgofildihdagmgoefodlccnlcnledddagmgoedddagfobdagedd'
	decrypted = ''
	for i in range(0, len(encrypted), 3):
		x = encrypted[i:i+3]
		decrypted += table3[x]

	print(decrypted)

if __name__ == '__main__':
	main()
```
```
keep in mind: its just the middle level
```

___

## Answer

flag: `keep in mind: its just the middle level`