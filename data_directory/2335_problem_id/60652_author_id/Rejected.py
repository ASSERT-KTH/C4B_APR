s=input()
if not('h' in s and 'e' in s and 'll' in s and 'o' in s):
    print("NO")
else:
   if not(s.index('h')<s.index('e')<s.index('ll')<s.index('o')):
      print("NO")
   else:
      print("YES")