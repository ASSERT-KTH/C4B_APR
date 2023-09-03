def main():
    a,b,c = map(int, input().split())
    if a<b:
        if c<=0:
            return "NO"
        else:
            while a!=b:
                a+=c
                if a>b:
                    return "NO"
            return "YES"
    else:
        if a==b:
            return "YES"
        if c>=0:
            return "NO"
        else:
            while a!=b:
                a+=c
                if a<b:
                    return "NO"
            return "YES"

print(main())