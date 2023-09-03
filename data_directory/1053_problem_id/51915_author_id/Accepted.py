n = int(input())
test = 0
i = 0
j = 0
x = True

# while y:
#     while x:
#         i += 1
#         test = i*4 + j*7
#         if test == n:
#             x = False
#             y = False
#         elif test > n:
#             i = 0
#             break
#
#     test = i*4 + j*7
#     if test == n:
#         x = True
#         y = True
#         break
#     elif test > n:
#         x = False
#         y = False
#     j += 1
#
# if not x and not y:
#     print(-1)
# else:
#     print(str(4)*i+str(7)*j)

j = 1
j_list = [0]
i_list = [0]
final_list = []
while test < n:
    test = 4*i + 7*j
    j_list.append(j)
    if n-test < 7:
        break
    j += 1

for j in j_list:
    i = (n-(j*7))/4
    if i.is_integer():
        if (n-(j*7))/4 >= 0:
            i_list.append(int(i))
            final_list.append((int(i), int(j)))

# print(final_list)

if final_list:
    final = []
    min_sum = 10**999
    for a, b in final_list:
        if a + b == min_sum:
            final.append((a, b))
        elif a + b < min_sum:
            final = [(a, b)]
            min_sum = a + b

    # print(final)
    min_b = 10**999
    a_final = 0
    for a, b in final:
        if b < min_b:
            min_b = b
            a_final = a

    print(str(4)*a_final + str(7)*min_b)

else:
    print(-1)