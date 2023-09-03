n = int(input())
if (n % 7) % 4 == 0 or (n % 4) % 7 == 0:
    if (n % 7) % 4 == 0 and (n % 4) % 7 != 0:
        print('4'*((n%7)//4)+'7'*(n // 7))
    else: 
        print('4'*(n // 4)+'7'*((n % 4)//7))
else:
    k = n
    ans1 = ''
    ans2 = ''
    while n > 0:
        ans1 += '7'
        ans2 += '4'
        k -=7
        n -= 4
        if (n % 7) % 4 == 0 or (n % 4) % 7 == 0:
            if (n % 7) % 4 == 0 and (n % 4) % 7 != 0:
                print(ans2+'4'*((n%7)//4)+'7'*(n // 7))
            else: 
                print(ans2+'4'*(n // 4)+'7'*((n % 4)//7))
            break
        if (k % 7) % 4 == 0 or (k % 4) % 7 == 0:
            if (n % 7) % 4 == 0 and (n % 4) % 7 != 0:
                print('4'*((n%7)//4)+'7'*(n // 7)+ans1)
            else: 
                print('4'*(n // 4)+'7'*((n % 4)//7)+ans1)      
            break