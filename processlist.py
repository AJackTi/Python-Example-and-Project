# AJack Ti
#30/11/2017

try:
	import psutil	
except:
	import os
	os.system('pip install psutil')

# listing all process in my machine
for proc in psutil.process_iter():
    print(proc)
    print(proc.name())
    if (proc.name() == "python.exe"):
        print proc.memory_maps()