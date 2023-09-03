x, y, z = list(map(int, input().split()))
ans1 = 2*x + 2*y
ans2 = x+z+y
ans3 = y+z+y+x
ans4 = y+z+z+y
print(min(ans1, ans2, ans3, ans4))