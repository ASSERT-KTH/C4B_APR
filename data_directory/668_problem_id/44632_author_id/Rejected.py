N = int(input())
S = ""
for i in range(N,0,-1):
    if S!= "":
        S=S+" that "
    if i%2 == 0:
        S=S+"I love"
    else:
        S=S+"I hate"
S=S+" it"
print(S)