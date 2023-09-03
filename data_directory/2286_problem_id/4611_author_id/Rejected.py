st = list(map(str,input().split()))

if len(st) > 1:
    if st[len(st)-1] != '?':
        if st[len(st)-1][-2] =='a'or st[len(st)-1][-2] =='e'or st[len(st)-1][-2] =='i'or st[len(st)-1][-2] =='o'or st[len(st)-1][-2] =='u'or st[len(st)-1][-2] =='y'or st[len(st)-1][-2] =='A'or st[len(st)-1][-2] =='E'or st[len(st)-1][-2] =='O'or st[len(st)-1][-2] =='I'or st[len(st)-1][-2] =='U'or st[len(st)-1][-2] =='Y':
            print("YES")
        else:
            print("NO")
    else:
        if st[len(st)-2][-1] =='a'or st[len(st)-2][-1] =='e'or st[len(st)-2][-1] =='i'or st[len(st)-2][-1] =='o'or st[len(st)-2][-1] =='u'or st[len(st)-2][-1] =='y'or st[len(st)-2][-1] =='A'or st[len(st)-2][-1] =='E'or st[len(st)-2][-1] =='O'or st[len(st)-2][-1] =='I'or st[len(st)-2][-1] =='U'or st[len(st)-2][-1] =='Y':
            print("YES")
        else:
            print("NO")
else:
    if st[0][-1]=='a' or st[0][-1]=='e' or st[0][-1]=='o' or st[0][-1]=='i' or st[0][-1]=='u' or st[0][-1]=='y' or st[0][-1]=='A' or st[0][-1]=='O' or st[0][-1]=='E' or st[0][-1]=='I' or st[0][-1]=='U' or st[0][-1]=='Y':
        print("YES")
    else:
        print("NO")


    
   # if st[len(st)-2][-1] == 'a' or st[len(st)-2][-1] == 'e' or st[len(st)-2][-1] == 'i' or st[len(st)-2][-1] == 'o' or st[len(st)-2][-1] == 'u':
    #    print("YES")
    #else:
     #   print("NO")