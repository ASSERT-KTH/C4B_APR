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
    if (times-1)%2 == 0:
      for i in range(1,times,2):
          anse = anse + " "+ loves + " "+hate
    else:
        for i in range(0,times-1,1):
            if(i%2 == 0):
                if(i+1 != times-1):
                  anse = anse +" "+ loves
                else:
                    anse = anse +" "+ love
            else:
                if(i+1 != times):
                  anse = anse +" "+ hates
                else:
                    anse = anse +" "+ hate
    print(anse)