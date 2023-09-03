from math import ceil

def calculNmbPave(n=0,m=0,a=0):
        try:
                l=int(ceil(n/a))
                h=int(ceil(m/a))
                return h*l
        except ValueError:
                print ("erreur de type")

n,m,a=list(map(int, input().split()))
print (calculNmbPave(n,m,a))