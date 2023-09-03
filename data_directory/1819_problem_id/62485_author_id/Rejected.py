data = input().split()

Y, K, N = int(data[0]), int(data[1]), int(data[2])

answer = []
counter = (K-Y)%K
if counter <= (N-Y) and counter > 0:
    answer.append(counter)

    counter += K
    while counter <= (N-Y):
        answer.append(counter)
        counter += K
    print(" ".join(map(str, answer)))
else:
    print('-1')