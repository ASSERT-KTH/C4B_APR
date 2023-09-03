import math

def main():
    a,b = map(int, input().split())
    return "YES" if a==b or abs(b-a)==1 else "NO"
print(main())