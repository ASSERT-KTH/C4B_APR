n = int(input())
kartu = 10
powarray = [1,2,3,4,5,6,7,8,9,11]
for i in range(len(powarray)):
    if(kartu + powarray[i]==n):
        print("4")
if(kartu + 10==n):
    print("15")
elif(n<=10 or n>21):
    print("0")