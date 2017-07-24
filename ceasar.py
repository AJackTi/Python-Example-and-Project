arr_a = []
arr_A = []

def init_arr():
    for i in range(97,123):
        arr_a.append(i)
    for i in range(65,91):
        arr_A.append(i)

def str_Input():
    str_input = str(raw_input(">"))
    return str_input

def cryto_ceasar(str_input):
    arr_output = []
    str_output = ''  # output
    for i in range(0,26): #key
        str_output=''
        for j in range(0,len(str_input)): #str_input
            if ord(str_input[j]) in range(97,123):
                for z in range(0,len(arr_a)): #arr_a
                    if str_input[j] == chr(arr_a[z]): # equal arr_a vs str_input[j]
                        if ord(str_input[j]) + i > 122: # outside scope a-z
                            index_a = z + i - 24
                            index_a-=2
                            str_output+=chr(arr_a[index_a])
                            break
                        else:
                            str_output+=chr(ord(str_input[j]) + i )
                            break
            elif ord(str_input[j]) in range(65,91):
                for z in range(0, len(arr_A)):
                    if str_input[j] == chr(arr_A[z]): #equal arr_A vs str_input[j]
                        if ord(str_input[j]) + i  > 90:
                            index_A = z + i - 24
                            index_A-=2
                            str_output+=chr(arr_A[index_A])
                            break
                        else:
                            str_output+=chr(ord(str_input[j]) + i)
                            break
            else:
                str_output+=str_input[j]
        arr_output.append(str_output)
    return arr_output


init_arr()
str_input = str_Input()
arr = cryto_ceasar(str_input)
count = 0
for i in arr:
    print "key=", count, "result: ", i
    count+=1