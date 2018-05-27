fileTypeNotSupport = ['.ADE', '.ADP', '.BAT', '.CHM', '.CMD', '.COM', '.CPL', '.DLL', '.DMG', '.EXE', '.HTA'
, '.INS', '.ISP', '.JAR', '.JS', '.JSE', '.LIB', '.LNK', '.MDE', '.MSC', '.MSI', '.MSP', '.MST', '.NSH', '.PIF', '.SCR', '.SCT'
, '.SHB', '.SYS', '.VB', '.VBE', '.VBS', '.VXD', '.WSC', '.WSF', '.WSH', '.CAB']

from os import walk
import os
import argparse

def listAllFile(directory): # Get file name of folder. 
    listPathFileMP4 = []
    for dirname, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            listPathFileMP4.append( os.path.join(dirname, filename))
    return listPathFileMP4

def checkFileType(arrFile):
    for item in arrFile:
        itemFileType = '.' + item.split('\\')[len(item.split('\\'))-1].split('.')[len(item.split('\\')[len(item.split('\\'))-1].split('.'))-1]
        if itemFileType in fileTypeNotSupport or itemFileType in [i.lower() for i in fileTypeNotSupport]:
            try:
                removeFile(item)
                print "[+] Remove File Success " + str(item)
            except:
                print "[-] Remove File Fail" + str(item)
    print "[+] Done"

def removeFile(pathFile):
    os.remove(pathFile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check Existence Of File")
    parser.add_argument("-d", dest="directory", help="Enter your directory")
    args = parser.parse_args()
    checkFileType(listAllFile(args.directory))

# AJack Ti
# 27/05/2018
