import math
def main():
    n = int(input())
    phib = [1, 1]
    ans = 0
    while(phib[-1] + phib[-2] <= n):
        phib.append(phib[-1] + phib[-2])
        ans += 1

    print(ans)
main()