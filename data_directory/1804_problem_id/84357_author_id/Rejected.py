stri=input()
b=[]
b=list(set(stri))
if len(b)%2==0:
    print("CHAT WITH HER!")
elif len(b)%3==0:
    print("IGNORE HIM!")