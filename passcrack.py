import md5

# 28/09/2017

counter = 1

pass_in = raw_input("Please enter the MD5 Hash: ")
pwfile = raw_input("Please enter the password file name: ") # file contain list of password
try:
	pwfile = open(pwfile, "r")
except Exception as e:
	print "\nFile Not Found"
	quit()

for password in pwfile:
	filemd5 = md5.new(password.strip()).hexdigest()
	#hexdigest() is returned as a string of length 32, containing only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments.
	print "Trying password number %d: %s" %(counter, password.strip())

	counter += 1

	if pass_in == filemd5:
		print "\nMatch Found. \nPassword is: %s" %password
		break
	else:
		print "\nPassword Not Found."
	