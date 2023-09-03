import sys
import collections 
sys.setrecursionlimit(30000)


def main():
    a,b,c = ([int(i) for i in input().split()])
    a = b*c + (b+c-1)*(a-1)
    print(a)
if __name__ == "__main__":
    ##sys.stdin = open('oddoreven.in','r')
    ##sys.stdout = open('oddoreven.out','w')
    main()
    ##sys.stdin.close()
    ##sys.stdout.close()