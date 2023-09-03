n = int( input())
k = int( input())

# print (n, k)
total_time = 240
remaining_time = total_time - k
result = 0
#print('The remaining time is ', remaining_time)

for i in range(1,n+1,1):
    #print('Trying for problem ', i)
    if remaining_time - 5*i >=0:
        remaining_time -= 5*i
        result += 1
    else:
        break


print(result)