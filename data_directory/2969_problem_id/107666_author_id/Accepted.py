def typecontest(s, v1, v2, t1, t2): 
    
    Firsttakes= v1*s + 2*t1
    Secondtakes= v2*s + 2*t2 
    
    if Firsttakes<Secondtakes: 
       print("First")
       
    elif Firsttakes > Secondtakes: 
        print("Second")
        
    else: 
        print("Friendship")
    
    return 
    


    


s, v1, v2, t1, t2=list(map(int, input().strip().split()))
typecontest(s,v1,v2,t1,t2)