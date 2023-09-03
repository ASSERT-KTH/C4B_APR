init_year = int(input())

i = init_year+1

while i <= 9000:
    str_i = str(i)
    digits_i = list(str_i)
    digits_i.sort()
    u_digits_i = list(set(str_i))
    u_digits_i.sort()
    if digits_i == u_digits_i:
        print (i)
        break
    i += 1