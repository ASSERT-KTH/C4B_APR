str_input = str(input())

if len(''.join(set(str_input))) % 2 == 0:
    print ('CHAT WITH HER!')
else:
    print('IGNORE HIM!')