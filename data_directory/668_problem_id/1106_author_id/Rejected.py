#in the name of god
#Mr_Rubik
#codeforces,problemset
n=int(input())
s=""
s+="I hate it"
for i in range(1,n):
    s+=" "
    if i%2==0:s+="I hate it"
    else:s+="I love it"
print(s)