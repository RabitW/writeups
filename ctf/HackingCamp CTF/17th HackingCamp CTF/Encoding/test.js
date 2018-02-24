
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
b = [15, 0, 13, 6, 7, 14, 3, 3, 0, 17, 8, 8, 18, 10, 8, 13, 6, 6, 14, 3, 4, 12, 15, 4, 17, 17, 14, 17];

var flag = "";

for (i = 0; i < b.length; i++) {
	b[i] = (( (a[0]).charCodeAt() + (b[i]) ) + []).replace("-", '').toString(10);
	flag += String.fromCharCode(b[i]);
}

console.log(flag);