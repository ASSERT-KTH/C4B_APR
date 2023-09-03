n, t = input().split(" ")
a = input()
for tt in range(int(t)):
      i = 0
      b = ""
      while i <= int(n)-1:
            if(i < int(n)-1):
                  if (a[i] == 'B' and a[i + 1] == 'G'):
                        b += 'GB'
                        i += 2
                  else:
                        b += (a[i])
                        i += 1
            else:
                  b += (a[i])
                  i += 1
      a = b
print(b)