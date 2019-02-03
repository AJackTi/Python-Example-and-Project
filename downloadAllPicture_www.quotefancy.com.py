from BeautifulSoup import BeautifulSoup
import urllib2, urllib, requests
import re

html_page = urllib2.urlopen("https://quotefancy.com/")
soup = BeautifulSoup(html_page)

setResult = set()

for link in soup.findAll('a'):
    if str(link.get('href')).startswith("http"):
        setResult.add(str(link.get('href')))

listResult = list(setResult)


for link in listResult:
    html_page = urllib2.urlopen(link)
    soup = BeautifulSoup(html_page)
    for sublink in soup.findAll('a'):
        if str(sublink.get('href')).endswith('.jpg'):
            url = "https://quotefancy.com" + str(sublink.get('href'))
            print "Downloading ..." + url
            r = requests.get(url)
            with open("Quotefancy-" + url.split("/")[4] + "-3840x2160" + '.jpg', 'wb') as f:
                f.write(r.content)

print "[+] Download Complete ... "

