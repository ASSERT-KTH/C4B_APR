#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 03:12:59 2017

@author: omaroove
"""


Word = input();
word = Word.lower()
def dot(word):
   return '.'.join(list(word))
Namee , s = "" , ""

for i in range(len(word)):
    if word[i] != 'O' and word[i] != 'o' and word[i] != 'I' and word[i] != 'i' and word[i] != 'U' and word[i] != 'u' and word[i] != 'E' and word[i] != 'e' and word[i] != 'A' and word[i] != 'a' :
        Namee+=word[i]
            
Res = dot(Namee)
print ("."+Res)