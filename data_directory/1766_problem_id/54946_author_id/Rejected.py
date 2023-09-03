inp = input()
sum = 0
cd = 0

lista = list()

for letter in inp:
    c = inp.count(letter)
    sum +=c

if sum == len(inp):
    print("0")
    cd = 100
elif c == len(inp):
    print (len(inp)-1)
    cd = 100
else:
    for j in range(len(inp)):
        for i in range(len(inp),0,-1):
            stri = inp[j:i]
            #print ("stri " + stri)
            w = inp.index(stri)
            new_str = inp[w+len(stri)-1:]
            #print("new " + new_str)
            if stri in new_str:
                lista.append(len(stri))

if cd != 100:
    print (max(lista))