s = input()
num = int(s)
n = len(s)
x = int(s[0]) 
ans = (x+1)*(10**(n-1))
print(ans-num)