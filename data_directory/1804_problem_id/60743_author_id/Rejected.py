word=input()
word=''.join(set(word))
if (len(word)%2==0):
    print("CHAT WITH HER")
else:
    print("IGNORE HIM!")