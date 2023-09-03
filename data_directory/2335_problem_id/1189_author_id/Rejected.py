def is_subseq(a, b):
    it = iter(y)
    return all(c in it for c in a)

if is_subseq('hello', input()):
    print("YES")
else:
    print("NO")