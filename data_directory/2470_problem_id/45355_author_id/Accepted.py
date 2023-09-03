prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
num=[int(i)for i in input().split()]
if prime[prime.index(num[0]) + 1] == num[1]:
    print("YES")
else:
    print("NO")