n = int(input());
m = int(input());
z = int(input());
x = 0;

for i in range(1, int(z/m + 1), 1):
    if(((m * i) % n) == 0):
        x += 1;
print(x);