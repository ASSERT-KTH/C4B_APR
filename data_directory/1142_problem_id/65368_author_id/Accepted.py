numbers=list(map(int, input().split()))
if(numbers[0]>0) and (numbers[0]<=100):
    if(numbers[1]<numbers[0]) and (numbers[2]<numbers[0]):
        if((numbers[0]-numbers[1])<=numbers[2]):
            print(numbers[0]-numbers[1])
        else:
            print(numbers[2]+1)