number = int(input())
if number >= 13:
    print(2**number - 100*(2**(number-13)))
else:
    print(2**number)