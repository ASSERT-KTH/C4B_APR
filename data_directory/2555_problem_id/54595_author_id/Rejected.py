if len(input()) < 7:
    print("NO")
elif input().find('0000000') != -1 or input().find('1111111') != -1:
    print("YES")
else:
    print("NO")