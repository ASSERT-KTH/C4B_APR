def main():
    hs = []
    t, f = 0, 0
    for i in range(8):
        hs.append( input().split() )
    
    for j in range(8):
        check = 0
        trak = 0
        for jj in range(8):
            if hs[j][0][jj] == "B": trak+=1
            if hs[jj][0][j] == "B": check+=1
        if trak>=8:t+=1
        if check>=8: t+=1
    if t==16: t = t/2
    print( t )

if __name__ == "__main__": main()