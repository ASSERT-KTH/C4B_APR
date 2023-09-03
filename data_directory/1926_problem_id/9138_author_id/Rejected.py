# python3
import sys, threading, os.path
import collections, heapq, math,bisect
import string
from platform import python_version
import itertools
sys.setrecursionlimit(10**6)
threading.stack_size(2**27)

def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    #--------------------------------INPUT---------------------------------
    n,m = list(map(int, input.readline().split()))
    lis = []
    temn,temm = n,m
    for i in range(n+m):
        if i ==0:
            if (n<m and temn>0) or (temn>0 and temm==0):
                lis.append(1)
                temn-=1
            else:
                temm-=1
                lis.append(2)
            continue
        if i%2==0:
            if lis[i-1]==1 and temn>0  or (temn>0 and temm==0):
                temn-=1
                lis.append(1)
            else:
                temm-=1
                lis.append(2)
        else:
            if lis[i-1]==2 and temn>0  or (temn>0 and temm==0):
                temn-=1
                lis.append(1)
            else:
                temm-=1
                lis.append(2)
    #print(lis)
    count1,count2=0,0
    for i in range(1,n+m):
        if lis[i]==lis[i-1]:
            count2+=1
        else:
            count1+=1
        
    
    output = str(count1)+" "+str(count2)
    #-------------------------------OUTPUT----------------------------------
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


if __name__ == '__main__':
    main()
#threading.Thread(target=main).start()