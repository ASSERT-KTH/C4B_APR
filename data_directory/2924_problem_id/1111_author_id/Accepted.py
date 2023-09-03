n = int(input())
s = input()
t = 0
for i in s:
    if i == '1':
        t += 1
    else:
        print(t,sep = '', end = '')
        t = 0
print(t,sep = '', end = '')