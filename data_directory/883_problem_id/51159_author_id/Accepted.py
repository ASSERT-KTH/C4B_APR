s = list()
inp = input()
for i in range(len(inp)):
  s.append(inp)
  inp = inp[1:] + inp[0]
  
print( len(set(s)) )