n, t = map(int, input().split())
ppl = list(input())
p = 0
for i in range(t):
    for z in range(len(ppl)-1):
        if p:
            p = 0
            continue
        if ppl[z] == "B" and ppl[z+1] == "G":
            ppl[z], ppl[z+1] = ppl[z+1], ppl[z]
            p = 1
ppl = "".join(ppl)
print(ppl)