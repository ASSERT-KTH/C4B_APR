arr = [int(x) for x in input().split()]
arr.sort()
if arr[0]==arr[1]==arr[2]:
    print(3*arr[0])
else:
    print(2*(arr[0]+arr[1]))