import random

def get_primes(n):
  numbers = set(range(n, 1, -1))
  primes = []
  while numbers:
    p = numbers.pop()
    primes.append(p)
    numbers.difference_update(set(range(p*2, n+1, p)))
  return primes

# primeslist = get_primes(1000)
primeslist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 521, 523, 541, 547, 557, 563, 569, 571, 577, 991, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 409, 929, 419, 421, 937, 941, 431, 433, 947, 439, 953, 443, 449, 967, 457, 971, 461, 463, 977, 467, 983, 479, 997, 487, 491, 499, 503, 509]

#==================================================================

def getStats():
  p = primeslist[random.randint(0,167)]
  q = primeslist[random.randint(0,167)]
  n = p*q
  phi = (p-1)*(q-1)
  e = 17
   
  return (n, phi, e)

"""

This code was in effort to keep e from being a factor of phi.
Was later just replaced with a larger prime number for e. (17)

 if phi%3 != 0:
  e = 3
  
 if phi%5 != 0:
  e = 5
  
 if phi%7 != 0:
  e = 7
 
"""

statsTuple = getStats()

def getPrivateKey():
  newPhi = statsTuple[1]
  newE = statsTuple[2]
  def euclid(num1, num2, num3, num4):
    if num3 ==1:
      key = num4
      return key
    else:
      newNum3 = num1 - ((num1//num3)*num3)
      newNum4 = (num2 - (num4*(num1//num3)))%newPhi
      return euclid (num3, num4, newNum3, newNum4)
  return euclid(newPhi, newPhi, newE, 1)
 

privateKey = getPrivateKey()

def encrypt(message): #<a class="yt-simple-endpoint style-scope yt-formatted-string" href="/results?search_query=%23returns">#returns</a> list of each char, encrpyted
  cipherList = []
  for ltr in message:
    encrpytedLtr = (ord(ltr)**statsTuple[2]) % statsTuple[0]
    cipherList.append(encrpytedLtr)
  return cipherList
 
def decrypt(cipherTextList):
  d = int(input("What's the private key?"))
  if d == privateKey:
    message = []
    for item in cipherTextList:
      decryptedLtr = chr((item**d) % statsTuple[0])
      message.append(decryptedLtr)
     
    print("Message:", ''.join(message))
    
  else:
    print("Invalid key")

if __name__ == "__main__":
  print primeslist
	# print getPrivateKey()
	# print encrypt("Hihi")
	# c = encrypt("Hihi")
	# decrypt(c)