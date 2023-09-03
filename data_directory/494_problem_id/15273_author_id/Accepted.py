#import pandas
def answer(n):
    res = ""
    for i in range(1, 371):
        res = res + str(i)
    return res[n -1]


print(answer(int(input())))