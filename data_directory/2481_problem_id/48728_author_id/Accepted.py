n = int(input())
row = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
if n<=5:
    print (row[n-1])
else:
    while n>5:
        n=(n-5)/2
    print(row[int(n)])