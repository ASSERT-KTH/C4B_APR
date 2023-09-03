def direct(num):
    return len(str(num)) == str(num).count('4') + str(num).count('7')
    
def indirect(num):
    for fac in [k for k in range(4, num+1) if num%k == 0]:
        if direct(fac): return 'YES'
    return 'NO'

print(indirect(int(input())))