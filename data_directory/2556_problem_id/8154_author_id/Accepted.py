n=0
s=""
def check():
    global n
    global s 
    t=0
    for i in range(0,len(s)//2):
      t*=10
      t+=7
    for i in range(0,len(s)//2):
      t*=10
      t+=4
    #print(t)
    if(int(s)>t):n+=2

def rec (i):
   global n
   global s
   j=i*10+4
   k=i*10+7
   #print(j,k)
   f1,f2=False,False 
   if len(str(j))==n: 
      #print(str(j),str(k))
      #print(str(j).count("4"))
      #print(str(j).count("7"))
      #print(str(k).count("4"))
      #print(str(k).count("7"))
      if j>=int(s)and str(j).count("4")==str(j).count("7"):f1=True
      if k>=int(s)and str(k).count("4")==str(k).count("7"):f2=True
      if f1 and f2:
        #print(j,f1,k,f2,min(j,k))
        return (min(k,j))
      elif f1:
        #print(j)
        return j
      elif f2:
        #print(k)
        return k
      else: 
        #print(1e15)
        return 1e15
       
   return min(rec(k),rec(j))

s=input()
n=len(s)+int(len(s)%2!=0)
if(len(s)%2==0):check()
print(rec(0))