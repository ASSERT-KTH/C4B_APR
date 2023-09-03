#!/usr/bin/env python 3

def main():
    string=input()
    temp=string[0].upper()+string[1:]
    if temp.isupper()==1:
        print(string.swapcase())
    else:
        print(string)

if __name__=='__main__':
    main()