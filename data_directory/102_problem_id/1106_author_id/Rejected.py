#in the name of god
#Mr_Rubik
#codeforces,problemset
for i in range(100):
    d1,d2,d3=map(int,input().split())
    mn=[(d1+d2+d1+d2),(d1+d3+d1+d3),(d2+d3+d2+d3),(d1+d3+d2)]
    mn.sort()
    print(mn[0])