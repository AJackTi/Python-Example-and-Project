import webbrowser
read_file = open('text_add_enter_file.txt', 'r')

for i in read_file.readlines():
	webbrowser.open_new_tab(i)