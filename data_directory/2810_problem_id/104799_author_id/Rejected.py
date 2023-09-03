MOD=10**9+7;
s=input();
ls=len(s);
step=0
numa=0;
ans=0;
i=0
while(i<ls):
    if(s[i]=="a"):
        numa=numa+1;i=i+1;
    else:
        step=step+(2**numa-1);i=i+1;
ans=step%MOD;
print(ans);