n, t = input().split()
seq = list(input())

for i in range(int(t)):
    newSeq = []
    is_change = False
    for j in range(int(n) - 1):
        if is_change:
            is_change = False
            continue
        if seq[j] == 'B' and seq[j + 1] == 'G':
            newSeq.append('G')
            newSeq.append('B')
            is_change = True
        else:
            newSeq.append(seq[j])
        if j == int(n) - 2:
            if len(newSeq) != len(seq):
                newSeq.append(seq[j + 1])
    seq = newSeq

print(''.join(seq))