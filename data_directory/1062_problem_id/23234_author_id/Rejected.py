n=input()
if n.count("4")==len(n):
    print("YES")
elif n.count("7")==len(n):
    print("YES")
elif n.count("4")+n.count("7")==len(n):
    print("YES")
else :
    print("NO")