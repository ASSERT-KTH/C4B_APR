#in the name of god
#Mr_Rubik
#codeforces,problemset
n=int(input())
if n==1:
    print("I hate it")
else:
    s=""
    for i in range(n-1):
        if i%2==0:s+="I hate that"
        else:s+="I love that"
        s+=" "
    if n%2==0 and n!=1:s+="I love it"
    if n%2==1 and n!=1:s+="I hate it"    
    print(s)