"""http://codeforces.com/problemset/problem/233/B"""

def s(x): return sum(map(int, str(x)))
def solve(n):
    l = 1; r = int(n ** 0.5)
    for x in range(max(1, r - 1), r + 1):
        if x * (x + s(x)) == n:
            return x
    return -1

def test():
    assert solve(2) == 1
    assert solve(110) == 10
    assert solve(4) == -1

if __name__ == '__main__':
    # test()
    print(solve(int(input())))