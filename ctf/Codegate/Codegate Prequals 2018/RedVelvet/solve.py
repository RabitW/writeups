import hashlib


def func1(a1, a2):
	if a1 * 2 * (a2 ^ a1) - a2 != 10858:
		return False
	if a1 <= 85 or a1 > 95 or a2 <= 96 or a2 > 111:
		return False
	return True

def func2(a1, a2):
	if a1 % a2 != 7:
		return False
	if a2 <= 90:
		return False
	return True

def func3(a1, a2):
	if a1 // a2 + (a2 ^ a1) != 21 or a1 > 99 or a2 > 119:
		return False
	return True

def func4(a1, a2):
	v2 = (a2 ^ a1 ^ a2) >> 32;
	v2 *= (0xffffffff+1)
	v2 += (a2 ^ a1 ^ a2);
	if (v2 % a2) + a1 != 137 or a1 <= 115 or a2 > 99 or a2 != 95 :
		return False
	return True

def func5(a1, a2):
	if ((a2 + a1) ^ (a1 ^ a2 ^ a1)) != 225 or a1 <= 90 or a2 > 89:
		return False
	return True

def func6(a1, a2, a3):
	if a1 > a2 :
		return False
	if a2 > a3 :
		return False
	if a1 <= 85 or a2 <= 110 or a3 <= 115 or ((a2 + a3) ^ (a1 + a2)) != 44 or (a2 + a3) % a1 + a2 != 161 :
		return False
	return True

def func7(a1, a2, a3):
	if a1 < a2 :
		return False
	if a2 < a3 :
		return False
	if a1 > 119 or a2 <= 90 or a3 > 89 or ((a1 + a3) ^ (a2 + a3)) != 122 or (a1 + a3) % a2 + a3 != 101 :
		return False
	return True

def func8(a1, a2, a3):
	if a1 > a2 :
		return False
	if a2 > a3 :
		return False
	if a3 > 114 or (a1 + a2) // a3 * a2 != 97 or (a3 ^ (a1 - a2)) * a2 != -10088 or a3 > 114 :
		return False
	return True

def func9(a1, a2, a3):
	if a1 != a2 :
		return False
	if a2 < a3 :
		return False
	if a3 > 99 or a3 + a1 * (a3 - a2) - a1 != -1443 :
		return False
	return True

def func10(a1, a2, a3):
	if a1 < a2 :
		return False
	if a2 < a3 :
		return False
	if a2 * (a1 + a3 + 1) - a3 != 15514 or a2 <= 90 or a2 > 99 :
		return False
	return True

def func11(a1, a2, a3):
	if a2 < a1 :
		return False
	if a1 < a3 :
		return False
	if a2 <= 100 or a2 > 104 or a1 + (a2 ^ (a2 - a3)) - a3 != 70 or (a2 + a3) // a1 + a1 != 68 :
		return False
	return True

def func12(a1, a2, a3):
	if a1 < a2 :
		return False
	if a2 < a3 :
		return False
	if a2 > 59 or a3 > 44 or a1 + (a2 ^ (a3 + a2)) - a3 != 111 or (a2 ^ (a2 - a3)) + a2 != 101 :
		return False
	return True

def func13(a1, a2, a3):
	if a1 > a2 :
		return False
	if a2 > a3 :
		return False
	if a1 <= 40 or a2 <= 90 or a3 > 109 or a3 + (a2 ^ (a3 + a1)) - a1 != 269 or (a3 ^ (a2 - a1)) + a2 != 185 :
		return False
	return True

def func14(a1, a2, a3):
	if a1 < a3 :
		return False
	if a2 < a3 :
		return False
	if a2 > 99 or a3 <= 90 or a1 + (a2 ^ (a2 + a1)) - a3 != 185 :
		return False
	return True

def func15(a1, a2, a3):
	if a2 < a3 :
		return False
	if a2 < a1 :
		return False
	if a3 <= 95 or a2 > 109 or ((a2 - a1) * a2 ^ a3) - a1 != 1214 or ((a3 - a2) * a3 ^ a1) + a2 != -1034 :
		return False
	return True


flag = ""

for a in range(1,128):
	for b in range(1,128):
		if func1(a, b):
			flag += chr(a) + chr(b)
			break

a = ord(flag[-1])
for b in range(1, 128):
	if func2(a, b):
		flag += chr(b)
		break

a = ord(flag[-1])
for b in range(1, 128):
	if func3(a, b):
		flag += chr(b)
		break

a = ord(flag[-1])
for b in range(1, 128):
	if func4(a, b):
		flag += chr(b)
		break

a = ord(flag[-1])
for b in range(1, 128):
	if func5(a, b):

		for c in range(1, 128):
			for d in range(1, 128):
				if func6(b, c, d):
					flag += chr(b) + chr(c) + chr(d)

a = ord(flag[-1])
for b in range(1, 128):
	for c in range(1, 128):
		if func7(a, b, c):
			flag += chr(b) + chr(c)

a = ord(flag[-1])
for b in range(1, 128):
	for c in range(1, 128):
		if func8(a, b, c):
			flag += chr(b) + chr(c)

a = ord(flag[-1])
for b in range(1, 128):
	for c in range(1, 128):
		if func9(a, b, c):
			flag += chr(b) + chr(c)

a = ord(flag[-1])
for b in range(1, 128):
	for c in range(1, 128):
		if func10(a, b, c):
			flag += chr(b) + chr(c)

a = ord(flag[-1])
for b in range(1, 128):
	for c in range(1, 128):
		if func11(a, b, c):
			for d in range(1, 128):
				for e in range(1, 128):
					if func12(c, d, e):
						flag += chr(b) + chr(c) + chr(d) + chr(e)

a = ord(flag[-1])
for b in range(1, 128):
	for c in range(1, 128):
		if func13(a, b, c):
			flag += chr(b) + chr(c)

a = ord(flag[-1])
for b in range(1, 128):
	for c in range(1, 128):
		if func14(a, b, c):
			for d in range(1, 128):
				for e in range(1, 128):
					if func15(c, d, e):
						s = flag + chr(b) + chr(c) + chr(d) + chr(e)

						s1 = hashlib.sha256(s.encode()).hexdigest()
						s2 = "0a435f46288bb5a764d13fca6c901d3750cee73fd7689ce79ef6dc0ff8f380e5"

						if s1 == s2:
							print(s)