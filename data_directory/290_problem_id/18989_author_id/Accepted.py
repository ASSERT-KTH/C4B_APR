nums = list(map(int, input().split()))
e = nums[0]
i = nums[1]
dmg = nums[2]
passed = False

if(dmg is e or dmg is i or dmg is 0):
    print("Yes")
else:
    index = 0
    while(e*index < dmg and i*index < dmg):
        if((dmg-e*index)%i is 0):
            passed = True
            break
        elif((dmg-i*index)%e is 0):
            passed = True
            break
        index += 1
    if(passed):
        print("Yes")
    else:
        print('No')