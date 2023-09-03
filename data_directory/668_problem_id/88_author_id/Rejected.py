a=int(input())-1
print('I hate ',end='')
while a:
    if a%2:print('that I love ',end='')
    else:print('that I hate ',end='')
    a-=1
print('it')