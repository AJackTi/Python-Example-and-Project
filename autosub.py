from os import walk
import os
import argparse

vidext = ['.avi', '.mkv', '.wmv', '.mp4', '.mpg', '.mpeg', '.mov', '.m4v']

def downloadSub(listPathFileMP4): # Auto download sub
    for file in listPathFileMP4:
        os.system("autosub " + file.replace(" ", "\ "))

def listAllFileMP4(directory): # Get file name of folder. 
    listPathFileMP4 = []
    for dirname, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename in vidext:
                listPathFileMP4.append( os.path.join(dirname, filename))
    return listPathFileMP4

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto Download Sub Title")
    parser.add_argument("-d", dest="directory", help="Enter your directory")
    args = parser.parse_args()
    if args.directory != None:
        downloadSub(listAllFileMP4(args.directory))
        print "[+] Success"
    else:
        print "[-] Error while process downloading"
