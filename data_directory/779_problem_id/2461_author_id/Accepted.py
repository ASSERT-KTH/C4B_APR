x = input()
n = int(x[:-1]) - 1
s = [4, 5, 6, 3, 2, 1][ord(x[-1]) - ord('a')]
print(n // 4 * 16 + n % 2 * 7 + s)