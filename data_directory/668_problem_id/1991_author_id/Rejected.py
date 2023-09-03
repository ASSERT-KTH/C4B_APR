i = int(input())
if (i - 1) % 2 == 0 and i > 2:
    print("I hate that I love that " * int((i - 1)/2) + "I hate it")
elif i == 1:
    print("I hate it")
elif i == 2:
    print("I hate that I love it")
else:
    print("I hate that I love that " * int((i - 2)/2) + "sI hate that I love it")