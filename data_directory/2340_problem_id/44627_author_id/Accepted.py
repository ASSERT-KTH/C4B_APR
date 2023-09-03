s = input()
num = 0
for char in s:
    if char >= 'a':
        num +=1
if num >= len(s)-num:
    print(s.lower())
else:
    print(s.upper())