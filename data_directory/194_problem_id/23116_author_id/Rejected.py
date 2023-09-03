# http://codeforces.com/problemset/problem/617/A


n = int(input())

count = 0

for i in range(1, 6):
  div = int(n/i)
  if div > 0:
    n -= div*i
    count += div

  if n == 0:
    break


print(count)

# five = int(n/5)

# if five > 0:
#   n -= five*5
#   count += five

# four = int(n/4)

# if four > 0:
#   n -= four*4
#   count += four


# three = int(n/3)

# if three > 0:
#   n -= three*3
#   count += three


# two = int(n/2)

# if two > 0:
#   n -= two*2
#   count += two


# one = int(n/1)

# if one > 0:
#   n -= one*4
#   count += one



# print(count)