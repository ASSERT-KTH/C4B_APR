times = int(input())
hate = "I hate it"
hates = "I hate that"
love = "I love it"
loves = "I love that"
anse = ''
if times ==1 :
    print(hate)
else:
        anse  = anse + hates
        for i in range(0,times-1,1):
            if(i%2 == 0):
                if(i+1 != times-1):
                  anse = anse +" "+ loves
                else:
                    anse = anse +" "+ love
            else:
                if(i+1 != (times-1)):
                  anse = anse +" "+ hates
                else:
                    anse = anse +" "+ hate
        print(anse)