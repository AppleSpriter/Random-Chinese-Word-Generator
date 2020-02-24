# -*- coding: UTF-8 -*-
import random
import re
import os

path1 = "./yuan/"
files = os.listdir(path1)

alllist = []

for file in files:
    file = "yuan/" + file
    with open(file,"r",encoding="utf-8") as f:
        tmplist = f.readlines()
    alllist.extend(tmplist)

listLen = len(alllist)
outputNum = 0

while(1):
    op = input("input any key to go next but 'q' to quit:")

    if(op=='q'):
        break

    else:
        outputNum += 1
        print("第" + str(outputNum) + "个词语为：",end="")

        randomNum = random.randint(0,listLen-1)
        string = str(alllist[randomNum])
        print(string)
        #print(re.sub([0-9], string, ""))

    
f.close()

