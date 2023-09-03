n=int(input())
arr=["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
try:
    print(arr[n-1])
except:
    for i in range(n):
        arr.append(arr[0])
        arr.append(arr[0])
        del arr[0]
    print(arr[0])