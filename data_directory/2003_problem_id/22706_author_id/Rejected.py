# -*- coding: utf-8 -*-
year=int(input())
unique=False

def checkUnique(year):
    checkList=[]
    for c in str(year):
        if c in checkList:
            return False
        checkList.append(c)
    return True

while not unique:
    if checkUnique(year):
        unique=True
    year+=1

print(year)