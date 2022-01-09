from os import walk
import os
import sys
import argparse
from functools import reduce
import operator
import time

vidext = ['.avi', '.mkv', '.wmv', '.mp4', '.mpg', '.mpeg', '.mov', '.m4v']
lasttime = 0


def downloadSub(listPathFileMP4):  # Auto download sub
    for file in listPathFileMP4:
        os.system("autosub " + '"' + file + '"')


def listAllFileMP4(directory):  # Get file name of folder.
    listPathFileMP4 = []
    for dirname, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if reduce(operator.xor, [filename.endswith(_) for _ in vidext]):
                try:
                    if (not os.path.isfile(os.path.splitext(os.path.join(dirname, filename))[0]+'.srt') and os.stat(os.path.splitext(os.path.join(dirname, filename))[0]+'.srt').st_size == 0):
                        pass
                except:
                    listPathFileMP4.append(os.path.join(dirname, filename))
    return listPathFileMP4


def loopDownload(directory):
    while(True):
        try:
            downloadSub(listAllFileMP4(directory))
            print('.')
            time.sleep(5)
        except KeyboardInterrupt:
            print('Thanks for using me')
            sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto Download Sub Title")
    parser.add_argument("-d", dest="directory", help="Enter your directory")
    args = parser.parse_args()
    if args.directory != None:
        loopDownload(args.directory)
