# AJack Ti
# 30/11/2017

import os, datetime

rootdir = "" # path Ex: C:\Users\blabla
searchdate = datetime.date.today()-datetime.timedelta(days=3)

for curr, dirs, files in os.walk(rootdir):
    for f in files:
        try:
            path = "%s/%s" % (curr, f)
            t = datetime.date.fromtimestamp(os.path.getmtime(path)) # get time 
            														# os.path.getmtime(path): return the last modification time of the file.
            														# datetime.date.fromtimestamp(): Return the local date corresponding to the POSIX timestamp


            if (t > searchdate):
            	print path
                print("found date %s on file %s" % (t,f))
        except Exception as e:
            no_op = 0