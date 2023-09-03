s = input()

l = list(s.lower())
k = list(s.lower())

#v stands for vowels 
v = ["a", "o", "y", "e", "u", "i"]

count = 0

for i in range(len(l)):
    if l[i] in v:
        k.remove(l[i])
        count = count - 1
    else:
        k.insert(i+count,".")
        count = count + 1
s2 = "".join(k)

print(s2)


##print(''.join('.'+l for l in input().lower() if l not in 'aeiouy'))