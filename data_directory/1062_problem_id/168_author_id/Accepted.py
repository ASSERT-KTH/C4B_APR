#a, b = map(int, input().split())
a = input()
num = a.count("4") + a.count("7")
num = str(num)
#print(num)
if len(num) == num.count("4") + num.count("7"): print("YES")
else : print("NO")