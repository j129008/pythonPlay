# -*- coding: UTF-8 -*-
import re
import sys
from collections import Counter
def printme(filename, endline):
    inFile = open(filename,"r",encoding="UTF-8")
    i = 0
    for line in inFile:
        if len(line) >= 0 and (re.match("^(\s)+$", line) == None):
            sys.stdout.write(i)
            print(line)
            i= i+1
            if i == endline:
                break
    inFile.close()

def printme7(filename, keyword):
    inFile = open(filename,"r",encoding="UTF-8")
    for line in inFile:
        if (keyword in line ):
            print(line)
    inFile.close()

def countJJ(filename, keyword):
    inFile = open(filename,"r",encoding="UTF-8")
    list = []
    for line in inFile:
        if (keyword in line ):
            p = re.compile("JJ[\s]+([^\)]+)")
            list.append( p.search(line).group(1) )
    cnt = Counter(list)
    print(cnt)
    inFile.close()
