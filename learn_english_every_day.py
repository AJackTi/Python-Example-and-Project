#Set environment in Linux if you use
##!/usr/bin/env python

# You must open cmd with administrator
# start -> windows powershell(admin)
 
import webbrowser, os, time, datetime, sys

def question_continue():
	print '[!] Do you want to continue learning English: ',
	print '[yes/no]:',
	str_input = raw_input('')
	if str_input in ['y','Y','YES','yes','Yes','yEs'] :
		return True
	else:
		return False

def main():
	print '[+] Loading toturial...'
	#"https://www.englishlistening.com/index.php/listen-to-passages/"
	link = ["hoc.elight.edu.vn", "rong-chang.com/supereasy/", "http://www.talkenglish.com/speaking/listidioms.aspx", "http://www.talkenglish.com/speaking/listinterview.aspx", "http://www.talkenglish.com/grammar/grammar.aspx", "http://www.talkenglish.com/speaking/listbasics.aspx", "http://www.talkenglish.com/speaking/listregular.aspx", "https://www.newsinlevels.com/", "https://www.memrise.com/course/342958/tu-vung-toeic-quan-trong-cap-1/"]

	for i in link:
		webbrowser.open_new_tab(i)
		time.sleep(5)

	os.system('cls') # clear screen cmd prompt

	now = datetime.datetime.now()
	hour = now.hour

	#set directory path 
	os.chdir('C:\\Windows\\System32')
	#delete file hosts prevent open website
	os.system('del C:\\Windows\\System32\\drivers\\etc\\hosts')

	while True:
		os.system('cls') # clear cmd in windows
						 # os.system('clear' in linux)
		print '|'
		os.system('cls')
		print '-'
		os.system('cls')
		print '\\'
		os.system('cls')
		print '/'
		os.system('cls')
		#after 3 hours, I must learn English about 3 hours
		if datetime.datetime.now().hours == hour+3: # copy file host consist of ip name and hostname to prevent open facebook.com and youtube.com ^^
			try:
				os.system('copy C:\\Users\\DUCTRONG_PC\\Desktop\\hosts C:\\Windows\\System32\\drivers\\etc')
			except Exception as e:
				print str(e)
			finally:
				print "End of proceed learning English every day^^. Have a good day for you. See you around!!!"
				break

if __name__ == '__main__':
	if question_continue():
		main()
	else:
		print '[+] Done. Maybe today you have learnt English'
		sys.exit()
