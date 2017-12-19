# 19/12/2017
from random import randint

# First, I will transfer message to list include number ascii of each of character of message
# After i encrypt that list => list include some number is encrypt
# m: initial message 
# e,n: public key
# c: data has been encrypted
# d: private key, is large number, multiplication of 2 prime numbers, it is very secure.

# check this number is prime
def is_prime(n):
    """ Check if n is a prime number

    @params:
    :n: integer number

    @returns: Boolean, True if n is prime number
             else False
    """
    return all(n%div and n%(div+2) for div in xrange(2, int(n**0.5)+1))

def init():
	p = randint(50, 1000)
	while not is_prime(p):
		p = randint(50, 1000)

	# p # q
	q = randint(50, 1000)
	while not is_prime(q) or p == q:
		q = randint(50, 1000)

	n = p*q

	phi_n = (p-1)*(q-1)

	return p,q,n,phi_n

# create private key d
def creat_private_key(phi_n, e):
	# out = []
	for i in range(10000):
		x = ((i * phi_n) + 1) / e
		y = (e * x) % phi_n
		if y == 1:
			# out.append(x)
			return x
	# return out
	# explanation: 
	# e*d mod phi(n) = 1
	# ex: 10 % 3 = 1
	# 		10 / 3 =3
	#		3*3+1=10
	#	e*d / phi(n) = ? => d = (?*phi(n)+1)/e
	#	e*d % phi(n) == 1 => d=...

# create public key e,n
def create_public_key(phi_n):
	# 1 < e < phi(n) and (e and phi_n are coprime)
	while True:
		# for i in list(range(2,phi_n)):
		i = randint(2, phi_n)
		if phi_n % i == 0:
			continue
		else:
			return i

# formula: m**e mod n = c => c=?
def encrypt(m,e,n):
	out = []
	try:
		for i in m:
			out.append( (i**e) % n )
	except Exception as e:
		pass

	return "".join(str(i) for i in out), out

# formula: c**d mod n = m => m=?
# c is list
def decrypt(c,d,n):
	out = []
	for i in c:
		out.append( (i**d) % n )

	return "".join(str(i) for i in out),out
	
# transfer list[ord(character of messages)] => list[number of character after it Sencrypt]
def transfer_ascii(str_input):
	lst_ouput = []
	for i in str_input:
		lst_ouput.append(ord(i))
	return lst_ouput

if __name__ == "__main__":
	p,q,n,phi_n = init()
	e = create_public_key(phi_n)
	
	# e != d. If not, error
	d = creat_private_key(phi_n, e)
	if e == d:
		while e == d:
			d = creat_private_key(phi_n, e)
	while d == None:
		p,q,n,phi_n = init()
		d = creat_private_key(phi_n, e)
	print p,q,n,phi_n
	print e, d


	lst_transfer = transfer_ascii("Hello I am AJack Ti")

	print lst_transfer

	# # encrypt
	str_encrypt, list_encrypt = encrypt(lst_transfer, e, n)
	print str_encrypt
	print list_encrypt

	# # decrypt
	str_decrypt, list_decrypt = decrypt(list_encrypt, d, n)
	print "decrypt:=> " + "".join(chr(i) for i in list_decrypt)	
# MY CODE IS VERY SLOW. BEACAUSE OF KEY IS SO BIG. HAHA