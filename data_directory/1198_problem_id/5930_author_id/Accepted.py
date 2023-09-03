k=0
j=0
word=input()
for i in range(len(word)):
    if(word[i]==("H") or word[i]==("Q") or word[i]==("9")):
       k=k+1
    else:
        j=j+1
if(k>=1):
    print("YES")
else:
    print("NO")