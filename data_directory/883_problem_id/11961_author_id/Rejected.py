s = input()
len({s[i:] + s[: i] for i in range(len(s))})