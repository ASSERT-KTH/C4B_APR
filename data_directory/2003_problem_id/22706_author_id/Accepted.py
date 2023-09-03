# -*- coding: utf-8 -*-
year=int(input())+1
unique=False

def checkUnique(year):
    checkList=[]
    for c in str(year):
        if c in checkList:
            return False
        checkList.append(c)
    return True

while True:
    if checkUnique(year)==True:
        break
    else:
        year+=1

print(year)