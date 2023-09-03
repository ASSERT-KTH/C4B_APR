s = list(map(int, input().split()))
dict = {}
if(s[0] == s[1] == s[2] == s[3]):
    print("3")
elif(s[0] == s[1] == s[2] or s[0] == s[1] == s[3] or s[0] == s[2] == s[3] or s[1] == s[2] == s[3]):
    print("2")
elif(s[0] == s[1] or s[0] == s[2] or s[0] == s[3] or s[1] == s[2] or s[1] == s[3] or s[2] == s[3]):
    print("1")
else:
    print("0")