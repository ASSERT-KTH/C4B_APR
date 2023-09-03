num = input()

fours = num.count('4')
sevens = num.count('7')
summ = fours + sevens

if summ==4 or summ==7:
    print ('YES')
else:
    print ('NO')