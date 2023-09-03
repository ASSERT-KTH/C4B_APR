def all_same(string):
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            return False
    return True


str = str(input())

for i in range(len(str) - 7):
    if all_same(str[i:i + 7]):
        print('YES')
        exit()
print('NO')