word=input()
jh=''.join(set(word))
if (len(jh)%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")