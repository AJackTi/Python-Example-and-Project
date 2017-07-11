introduce = """  
                     .-"``"-.
                    /______; \\
                   {_______}\|
                   (/ a a \)(_)
                   (.-.).-.)
      _______ooo__(    ^    )____________
     /             '-.___.-'             \\
    |        _   _   _   _   _   _        |
    |       / \ / \ / \ / \ / \ / \       |
    |      ( C | a | e | S | a | r )      |
    |       \_/ \_/ \_/ \_/ \_/ \_/       |
    |					                  |
     \________________________ooo________/
                   |_  |  _|  
                   \___|___/
                   {___|___}
                    |_ | _|
                    /-'Y'-\\
                   (__/ \__)
                   
"""

#convert string to char and add key
def convert(key, str):
    count = 0
    arr = [None] * len(str)
    while count < len(str):
        flag = True
        arr.pop(0)
        try:
            int(chr(ord(str[count])))
        except ValueError:
            flag = False
        if flag == True:
            arr.append(str[count])
        else:
            arr.append(chr(ord(str[count]) + key))
        count += 1
    new_str = ''
    for i in arr:
        new_str += i
    print "==>Result: ", new_str

def convertall(str):
    new_array = [None]
    new_str = ''
    for i in range(0, 27):
        new_array.append(new_str)
        new_str = ''
        for a in str:
            flag = True
            try:
                int(chr(ord(a)))
            except ValueError:
                flag = False
            if chr(ord(a) + i) == '{':
                new_str += 'a'
            elif chr(ord(a) + i) == '|':
                new_str += 'b'
            elif chr(ord(a) + i) == '[':
                new_str += 'A'
            elif chr(ord(a) + i) == '\\':
                new_str += 'B'
            elif flag == True:
                new_str += a
            else:
                new_str += chr(ord(a) + i)
    count = 0
    for i in new_array:
        print "key ", count, ":", str, "==>", i
        count += 1


def Menu():
    Flag = True
    while True:
        print introduce
        print "Welcome to CaeSar Cipher"
        print "Select 1, 2 or 3"
        print """ 
        1. Decode with key
        2. Decode all key
        3. Exit
        """

        se = raw_input(">")
        se = int(se)
        if se==1:
            str = raw_input("Input > ")
            key = raw_input("number > ")
            try:
                key = int(key)
            except ValueError as e_message:
                print e_message
                print "key is number type integer"

            if key in range(0, 26):
                print "key done"
            else:
                print "key error, key must in (0..26)"
                print "Try Again!!!"
                continue
            convert(key, str)
            print "Do you want continue?"
            print "Y: Yes or N: No"
            ch = raw_input(">")
            ch = ch.lower()
            if ch == 'n':
                exit(0)
        elif se==2:
            str = raw_input("Input > ")
            print "All key from 0 to 25 show:"
            convertall(str)
            print "Do you want continue?"
            print "Y: Yes or N: No"
            ch = raw_input(">")
            ch = ch.lower()
            if ch == 'n':
                exit(0)

        elif se==3:
            print "Bye"
            exit(0)
        else:
            print "Your select error! Try again!"
            print "Y: Yes or N: No"
            ch = raw_input(">")
            ch=ch.lower()
            if ch == 'n':
                exit(0)

Menu()