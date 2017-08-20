import webbrowser
import time

query = raw_input("Enter your Google query: ")
url1 = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % str(query) # in google
url2 = "https://vn.search.yahoo.com/search;_ylt=A2oKmLjSKplZFDIAuy.BdHRG;_ylc=X1MDMTE4MjAzNzEyMQRfcgMyBGZyAwRncHJpZANzd3Nxc25uclRsU25PRC5IQjlodjNBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4Ddm4uc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAM2BHF1ZXJ5A2hhY2tlcgR0X3N0bXADMTUwMzIxMDIxMA--?p=%s" % str(query) + "&fr=sfp&fr2=sb-top-vn.search&iscqry=" # in yahoo
url3 = "https://www.bing.com/search?q=hacker&qs=n&form=QBLH&sp=-1&pq=%s&sc=8-6&sk=&cvid=E7A46F63AD41407295BD029765CB9EF3" % str(query) # in Bing
url4 = "http://www.ask.com/web?q=%s&o=0&qo=homepageSearchBox" % str(query) # in ask.com
url5 = "https://search.aol.com/aol/search?s_chn=prt_bon&q=%s&s_it=comsearch" % str(query) # in search.aol.com
url6 = "https://www.wolframalpha.com/input/?i=%s" % str(query) # in wolframalpha.com
url7 = "https://duckduckgo.com/?q=%s&t=hb&ia=web" % str(query) # in duckduckgo.com
url8 = "https://web.archive.org/web/*/%s" % str(query) # in web.archive.org
url = [url1, url2, url3, url4, url5, url6, url7, url8]
# open in webbrowser
for i in url:
	webbrowser.open_new_tab(i)
	time.sleep(2)
