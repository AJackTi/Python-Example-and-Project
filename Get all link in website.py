# AJack Ti
# 30/11/2017
# Get all links in a page html

from HTMLParser import HTMLParser
import urllib2

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == "a"):
            for a in attrs:
                if (a[0] == 'href'):
                    link = a[1]
                    if (link.find('http') >= 0):
                        print link
                        newParse = myParser()
                        newParse.feed(link)

url = "https://www.newsinlevels.com/" # Your website that you want to get all links
request = urllib2.Request(url)
handle = urllib2.urlopen(request)
parser = myParser()
parser.feed(handle.read())