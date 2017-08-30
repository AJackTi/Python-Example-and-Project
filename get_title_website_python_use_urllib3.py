import urllib3,re, certifi

http = urllib3.PoolManager(
	cert_reqs='CERT_REQUIRED',
	ca_certs=certifi.where())

try:
	r = http.request('GET', 'http://www.python.org')
except Exception as e:
	print str(e)

print r.status # if r.status == 200 website normally
				# if r.status == 404 website not found
data = r.data # very huge code

regex = '<title>(.+?)</title>'
reg = re.compile(regex) # apply regex 
title = re.findall(reg, data)
print title