from hashlib import md5

secret_key = "ckczppom"
prefix = "00000"
# prefix = "000000"  # Part 2 input

i = 1
while True:
	h = md5((secret_key + str(i)).encode('utf-8')).hexdigest()
	if h.startswith(prefix):
		print(i)
		break
	i += 1
