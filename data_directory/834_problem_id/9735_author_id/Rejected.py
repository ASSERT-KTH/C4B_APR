import math
def main():
    n = int(input())
    phi = 0.6180339887498948482
    ans = 0
    while n > 1:
        n = round(n * phi)
        ans += 1
    print(ans)
main()