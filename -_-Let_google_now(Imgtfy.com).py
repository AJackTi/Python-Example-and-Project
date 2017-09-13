import webbrowser, time

# get html in web bu python
# get link in http://lmgtfy.com/(after click button [shorted link])
# Return link =]]

Key = str(raw_input("Enter your key you want to ask: "))

# array link
array_link = ['http://lmgtfy.com/?q='+Key, 'http://lmgtfy.com/?t=i&q='+Key,
              'http://lmgtfy.com/?t=v&q='+Key, 'http://lmgtfy.com/?t=m&q=game'+Key,
              'http://lmgtfy.com/?t=n&q='+Key, 'http://lmgtfy.com/?t=s&q=game'+Key,
              'http://lmgtfy.com/?t=b&q='+Key, 'http://lmgtfy.com/?t=f&q='+Key,
              'http://lmgtfy.com/?t=sc&q='+Key]

for i_array in array_link:
    try:
        webbrowser.open_new_tab(i_array)
    except Exception,e:
        print "[!] Netword Error. Please check it now."
        print e.message
    time.sleep(15)

print "[+] Done. You dont know google is free ^^. Finish"