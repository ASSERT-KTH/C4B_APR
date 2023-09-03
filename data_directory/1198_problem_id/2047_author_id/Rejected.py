x = input()
i = 0
z = "NO"
for i in range(len(x)):
    if(x[i] == 'H' or x[i] == 'Q'):
        z = "YES"
    i += 1
print(z)