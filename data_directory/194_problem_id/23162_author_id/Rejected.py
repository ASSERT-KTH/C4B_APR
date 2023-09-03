## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""
#
#if str == type(varA) or str == type(varB):
#    print("string involved")
#elif varA > varB:
#    print("bigger")
#elif varA == varB:
#    print("equal")
#else:
#    print("smaller")
#
#s = 'azcbobobegghakl'
#i = 0
#for l in s:
#    if l in 'aeiou':
#        i += 1
#print("Number of vowels:",i)
#
#r = 'bob'
#n = 0
#if r in s:
#    for j in range(len(s)-2):
#        if r == s[j:(j+3)]:
#            n += 1
#print("Number of times bob occurs is:",n)
#
#i = -1
#while True:
#    i += 1
x = int(input(''))
if x % 5 == 0:
    n = x/5
else:
    n = x//5 + 1
print(n)