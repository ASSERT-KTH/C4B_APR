n = int(input())
#n, m = map(int, input().split())
s = input()
#c = list(map(int, input().split()))
if (n % 2 == 0 and s.count('4') + s.count('7') == n and 
    int(s[:n // 2]) == int(s[n // 2:])):
    print('YES')
else:
    print('NO')