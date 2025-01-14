#!/usr/bin/python

import os
import sys
import glob
import codecs

inputdir = "."

if len(sys.argv) >= 2:
    inputdir = sys.argv[1]

def processdir(dir):
    dirList = glob.glob(dir)
    wordcount = {}
    for f in dirList:
        wordcountfile(f, wordcount)
    for w in wordcount:
        print(w, wordcount[w])

def wordcountfile(f, wordcount):
    file = codecs.open(f, "r", "utf-8")
    for word in file.read().split():
        word = word.lower()
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    file.close()
    return wordcount

if __name__ == "__main__":
    processdir(inputdir)
