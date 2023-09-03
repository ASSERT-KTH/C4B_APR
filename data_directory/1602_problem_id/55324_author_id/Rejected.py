if __name__ == "__main__":
    x, t, a, b, da, db = map(int, input().split())
    found = False
    if x == 0:
        found = True
    for i in range(t):
        for j in range(t):
            if a - i * da + b - j * db == x:
                found = True

    if found:
        print("YES")
    else:
        print("NO")