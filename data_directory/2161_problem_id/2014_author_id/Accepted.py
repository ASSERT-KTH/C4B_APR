########## the tic tac toe program simulations codeforces 3B
def count(M):
    count=[0]*3
    for i in range(3):
        for j in range(3):
            if M[i][j]=='X':
               count[0]+=1
            elif M[i][j]=='0':
               count[1]+=1
            else:
               count[2]+=1
    return count
    
#Check if winner is possible or not
def winner(M,c,k):
    s=k*3
    win=False
    if M[0][0]+M[0][1]+M[0][2]==s or M[1][0]+M[1][1]+M[1][2]==s or M[2][0]+M[2][1]+M[2][2]==s or M[0][0]+M[1][0]+M[2][0]==s or M[0][1]+M[1][1]+M[2][1]==s or M[0][2]+M[1][2]+M[2][2]==s or M[0][0]+M[1][1]+M[2][2]==s or M[0][2]+M[1][1]+M[2][0]==s :
       # 8 possible ways to win !
       win=True
    # return whether such a winning combination exists or not
    return win
       
def illegal(M,c):
    #It is illegal to have both as winners.
    illegal=False
    #CASE 1: Both winners
    a=winner(M,c,'X')
    b=winner(M,c,'0')
    if a and b:
       illegal=True
    #CASE 2: No of moves of X can be 1 more or equal
    if c[0]<c[1] or c[0]-c[1]>=2:
       illegal=True
    #CASE 3: '0' can win only when both have same count:
    if b and c[0]==c[1]+1:
       illegal=True
    #CASE 4: 'X' can win only when count of it is one more than '0':
    if a and c[0]==c[1]:
       illegal=True          
    return illegal
 
def next(c):
    if c[0]==c[1] and c[2]>0:
       return "first"
    elif c[0]==c[1]+1 and c[2]>0:
       return "second"
    return None   

def draw(M,c):
    if c[2]==0 and winner(M,c,'X')==False and winner(M,c,'0')==False:
       return "draw"
    return None             
                  
def winner2(M,c):
    a=winner(M,c,"X")
    b=winner(M,c,"0")
    if a and b==False:
       return "first"
    elif b and a==False:
       return "second"
    return None

def tester():
    M=[]
    for i in range(3):
        x=input()
        x=[i for i in x]
        M.append(x)
    #print("Matrix",M)
    c=count(M)
    #print("Count",c)
    ill=illegal(M,c)
    #Step 1: Check if it is valid or not
    if ill:
       #print("STEP1")
       print("illegal")
       return None
    #Step 2: if it is valid then see whether there is some winner   
    if winner2(M,c) is not None:
       #print("STEP2")
       print("the "+winner2(M,c)+" player won")
       return None
    #Step 3: check if the game is a draw   
    if draw(M,c) is not None:
       #print("STEP3")
       print("draw")
       return None
    #Step 4: Now predict next move:
    if next(c) is not None:
       #print("STEP4")
       print(next(c))
             
tester()