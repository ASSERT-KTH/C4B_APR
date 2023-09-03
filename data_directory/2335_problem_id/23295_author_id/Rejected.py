s=str(input())
p = ['h','e','l','l','o']
def compare(inputArray, compareArray):
  temp = 0
  n=len(inputArray)
  for item in compareArray:
    while temp < n:
      if s[temp] == item:
        if item == p[len(p)-1]:
          return print('YES')
        if temp != n-1 and item != p[len(p)-1] and  item == p[len(p)-1]:
          return print('NO')
        temp += 1
        break
      elif temp == n-1:
        return print('NO')
      # elif temp != n-1 and item != p[len(p)-1]:
      #   return print('NO')
      temp += 1

compare(s,p)