f = open("css3_property_table.txt", "r")
css3_prob_table = f.read().split("\n")
f.close()

flag_table = "-{HFCzrokebatmlf_usni}Tdc"

css3_prob_table2 = []
for css3_prop in css3_prob_table:
	is_ok = True
	for char in css3_prop:
		if char not in flag_table:
			is_ok = False
	if is_ok:
		css3_prob_table2.append(css3_prop)

flag_table2 = []
for char in flag_table:
	if char not in "HarekazeCTF{}":
		flag_table2.append(char)

css3_prob_table3 = []
for css3_prop1 in css3_prob_table2:
	for css3_prop2 in css3_prob_table2:
		maybe_flag = "HarekazeCTF{" + css3_prop1 + "_" + css3_prop2 + "}"
		is_ok = True
		for char in flag_table:
			if char not in maybe_flag:
				is_ok = False
				break
		if is_ok:
			print(maybe_flag)