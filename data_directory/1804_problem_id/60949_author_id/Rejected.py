username = input()
num = 0
for i in range(len(username)):
    for a in range(0,i):
        if username[i] == username[a]:
            num -= 1
    num += 1
if num%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")