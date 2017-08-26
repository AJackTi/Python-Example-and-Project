import webbrowser

input = raw_input("Enter your word to serch: ")

google_translate = "https://translate.google.com/?hl=vi#en/vi/" + input 
google_new = "https://news.google.com/news/search/section/q/" + input + "/" + input + "?hl=en&ned=us"
google_image = "https://www.google.com/search?biw=1366&bih=648&tbm=isch&sa=1&q=" + input + "&oq=" + input + "&gs_l=psy-ab.3..0j0i67k1l2j0.215902.216914.0.219357.9.6.0.0.0.0.475.475.4-1.1.0....0...1.1.64.psy-ab..8.1.475.eeZqv0U1j9s"

link = [google_translate, google_new, google_image]
for i in link:
	webbrowser.open_new_tab(i)