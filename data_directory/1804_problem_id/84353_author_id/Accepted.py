def chat(s):
    x = set([i for i in s])
    if len(x) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
s = input()
chat(s)