fin=open("input.txt")
fout=open("output.txt",'w')
n,m=map(int,fin.read().split())
fout.write(((n*m)//2))