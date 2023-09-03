#problem 131A
initial=input()
answer=""
if initial.isupper():
  answer=initial.lower()
elif initial[1:].isupper() or initial[0].islower():
  for i in range(0,len(initial)):
    if i==0:
      answer+=initial[i].upper()
    else:
      answer+=initial[i].lower()
else:
  for i in range(0,len(initial)):
    answer+=initial[i]
print(answer)