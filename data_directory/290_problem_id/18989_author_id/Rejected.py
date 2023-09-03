nums = list(map(int, input().split()))
e = nums[0]
i = nums[1]
dmg = nums[2]

def check(a, b, dmg, index):
    if(a*index > dmg):
        return False
    
    if((dmg-a*index)%b is 0):
        return True
    
    return check(a, b, dmg, index+1)


if(dmg is e or dmg is i or dmg is 0):
    print("Yes")


elif(check(e, i, dmg, 1) or check(i, e, dmg, 1)):
    print("Yes")
else:
    print("No")