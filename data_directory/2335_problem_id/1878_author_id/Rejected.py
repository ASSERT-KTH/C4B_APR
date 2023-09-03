def main():
    s = input()
    flag = "hello"
    id = 0
    for i in flag:
        a = s.find(i, id, len(s)-id)
        # print(s[id:len(s)])
        if a == -1:
            return False
        id = a
    return True

ans = main()
if ans:
    print("YES")
else:
    print("NO")