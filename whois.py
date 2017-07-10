#!/usr/local/lib/python2.7/dist-packages/whois/__init__.pyc
import whois

w = whois.whois( 'google.com' )

# w = whois.whois( 'ip target' )

# print out the expiration date
print w.expiration_date 

print w.text

print w
