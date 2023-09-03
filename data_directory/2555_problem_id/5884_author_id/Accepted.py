st=input("");
length=len(st);
count=0;
#print(length)
if length<7:
    print("NO")
else:
    for i in range(length):
        if i ==0:
            continue;
        if st[i]==st[i-1]:
            count=count+1
            #print(count)
            if count>=6:
                print("YES")
                break;
              
        else:
              if count>=6:
                print("YES")
                break;
              
              count=0
        
    if count < 6:
        print("NO");