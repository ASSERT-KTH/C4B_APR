n = int(input())
s = [len(st) for st in input().split('0')]
if s[-1] == 0:
    del s[-1]
print("".join(str(x) for x in s))