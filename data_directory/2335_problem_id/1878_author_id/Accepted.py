def main():
    s = input()
    flag = "hello"
    id = -1
    for i in flag:
        a = s.find(i, id+1)
        # print(s[id:len(s)])
        # print(a)
        if a == -1:
            return False
        id = a
    return True

ans = main()
if ans:
    print("YES")
else:
    print("NO")