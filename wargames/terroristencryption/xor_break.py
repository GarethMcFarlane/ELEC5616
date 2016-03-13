m1 = "Someone's sniffing around. Destroy the files!"

c1 = [98, 126, 125, 9, 232, 74, 154, 193, 5, 74, 11, 98, 192, 185, 198, 185, 128, 214, 126, 60, 221, 237, 222, 152, 189, 70, 159, 16, 41, 122, 200, 153, 196, 27, 206, 192, 45, 79, 241, 212, 111, 70, 126, 107]

c2 = [101, 121, 117, 76, 215, 86, 154, 149, 31, 14, 29, 98, 221, 248, 211, 240, 157, 193, 59, 56, 204, 234, 139, 159, 170, 72, 222, 32, 108, 90, 245, 191, 139, 83, 220, 135]

# XOR the two ciphertexts together to get the XOR of m1 and m2. Use the shorter length array.
result = [0] * len(c2)
index = 0
for i in c2:
	result[index] = c1[index] ^ i
	index += 1

# Using the XOR of m1 and m2, now XOR it with m1 to "undo" m1 and get m2 back.
m2 = ""
index = 0
for ch in m1:
	if (index >= len(result)):
		break
	m2 += chr(result[index] ^ ord(ch))
	index += 1

print(m2)
