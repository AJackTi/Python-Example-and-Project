from BeautifulSoup import BeautifulSoup
import urllib2, urllib, requests
import re, execjs
import js2py

# js = """$(".loadmore").click();"""

# for num in range(10):
#     result = js2py.eval_js(js)

html_page = urllib2.urlopen("https://quotefancy.com/")
soup = BeautifulSoup(html_page)

setResult = set()

for link in soup.findAll('a'):
    if str(link.get('href')).startswith("http"):
        setResult.add(str(link.get('href')))

listResult = list(setResult)

count = 0

for link in listResult:
    html_page = urllib2.urlopen(link)
    soup = BeautifulSoup(html_page)
    for sublink in soup.findAll('a'):
        if str(sublink.get('href')).endswith('wallpaper.jpg'):
            count += 1
            url = "https://quotefancy.com" + str(sublink.get('href'))
            print "Downloading ..." + url
            r = requests.get(url)
            with open(str(count) + '.jpg', 'wb') as f:
                f.write(r.content)

print "[+] Download Complete ... "

