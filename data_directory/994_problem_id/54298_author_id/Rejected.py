from math import ceil

def calculNmbPave(n=0,m=0,a=0):
        try:
                l=int(ceil(n/a))
                h=int(ceil(m/a))
                return h*l
        except ValueError:
                print ("erreur de type")

print (calculNmbPave(6,6,4))