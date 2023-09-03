str = input()
ar = ['h', 'e', 'l', 'l', 'o']
i = 0
for j in str:
    if i == len(ar):
        break
    if(j == ar[i]):
        i += 1
if i == len(ar):
    print("YES")
else:
    print("NO")