def chat(s):
    x = set([i for i in s])
    if len(x) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
while 1:
    s = input()
    if s != EOF:
        chat(s)
    else:
        break