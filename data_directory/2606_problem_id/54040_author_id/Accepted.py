n, k = map(int, input().split())

chars_dis = (n//k +1) * [chr(i + 97) for i in range(k)]
print(''.join(chars_dis[:n]))
# res = chars_dis[random.randint(0,len(chars_dis)) - 1]
# for i in range(1,n):
#     while True:
#         x = chars_dis[random.randint(0, len(chars_dis)) - 1]
#         if x != res[i-1]:
#             res += x
#             break
# print(res)
#