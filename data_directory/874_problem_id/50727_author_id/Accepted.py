def get_number(k):

    current = 1
    div = 1
    while True:

        if k%div == 0:
            current += 1
            div *= 2
        else:
            return current-1




inp = input()
n,k = inp.split(" ")
print(get_number(int(k)))