import char_meta as c
import gmpy2

def pow_mod(a, z, n):
	a1 = a
	z1 = z
	x = 1
	while z1 != 0:
		while (z1 % 2) == 0:
			z1 = z1 // 2
			a1 = (a1 * a1) % n

		z1 -= 1
		x = (x * a1) % n

	return x

def check_keys(q, p, h, x, k):
	if not gmpy2.is_prime(q):
		raise ValueError("q is not prime")
	if not gmpy2.is_prime(p):
		raise ValueError("p is not prime")

	if (p-1) % q != 0:
		raise ValueError("q is not a divider of p-1")

	if not (0 < x < q):
		raise ValueError(f"x not in range (0, {q})")

	if not (1 < h < p-1):
		raise ValueError(f"h not in range (1, {p-1})")

	if not (0 < k < q):
		raise ValueError(f"k not in range (0, {q})")

def read_file(path):
	with open(path, "r") as f:
		file_content = f.read()

	return file_content
def read_binary_file(path):
	file_content = ""
	with open(path, "rb") as f:
		file_content = f.read()

	content_code_list = [char for char in file_content]
	return content_code_list

def write_to_file(path, data, sign):
	char_data = ''.join([c.my_chr(char) for char in data])
	sign_str = "\n" + str(sign)
	with open(path, "w") as f:
		f.write(char_data)
		f.write(sign_str)

def get_hash(data, q):
	start_h = 100
	temp = 100
	res = []

	for byte in data:
		temp = pow(start_h + byte, 2, q)
		res.append(temp)
		start_h = temp
	return res, temp


def get_dsa(file_data, q, p, h, x, k):
	g = pow(h, (p-1)//q, p)
	
	r = pow(g, k, p) % q
	hash_value = get_hash(file_data, q)

	s = int(int(pow(k, q-2)) * (hash_value[1] + x*r) % q)

	if r == 0 or s == 0:
		raise ValueError("r or s is equal to 0, try with another value of k")
	
	return r,s, hash_value

def check_dsa(file_data, r, s, q, p, h, x):
	g = pow(h, (p-1)//q, p)

	w = pow(s, q-2, q)
	hash_value = get_hash(file_data, q)
	u1 = (hash_value[1] * w) % q
	u2 = (r * w) % q
	y = pow(g, x, p)
	v = (pow(g, u1) * pow(y, u2) % p) % q
	
	return v, hash_value[1]

def create_file_signature(in_file, q, p, h, x, k):
	try:
		lastslash = in_file.rfind("/")
		partpath = in_file[0:lastslash] + "/"
		point = in_file.rfind(".")
		filename = in_file[lastslash+1:point]
		filename = "signed_"+filename
		new_path = partpath + filename + ".txt"

		contents = read_binary_file(in_file)
		r, s, hash_value = get_dsa(contents, q, p, h, x, k)
		write_to_file(new_path, contents, f"{r},{s}")
		
		return r, s, hash_value[1], new_path
	except:
		raise ValueError("Error in signing file")

def check_file_signature(path, q, p, h, x):
	data = read_file(path)
	data = data[::-1].split("\n", 1)[::-1]

	new_data = []
	for item in data:
		new_data.append(item[::-1])
	sign = new_data.pop().split(",")
	
	r = int(sign[0])
	s = int(sign[1])

	file_data = []
	for string in new_data:
		for char in string:
			file_data.append(c.my_ord(char))
	v, hash_value = check_dsa(file_data, r, s, q, p, h, x)
	
	return r, v, hash_value
#contents = read_binary_file("/Users/roman/TI/lab4/test.txt")
#result = get_hash(contents, 593)

#result_dsa = get_dsa(contents, 593, 3559, 3, 17, 23)
#check_dsa(contents, result_dsa[0], result_dsa[1], 593, 3559, 3, 17)


#create_file_signature("/Users/roman/TI/lab4/test.txt", 433, 19919, 2, 11, 17)

#check_file_signature("/Users/roman/TI/lab4/test1.txt", 433, 19919, 2, 11)






