class Number:
	def main(self):
	    sum=0
	    sums=0
	    n=int(input())
	    for i in range(2,n):
	        s=n
	        while(s>0):
	            sum=sum+(s%i)
	            s=int(s/i)
	        print(sum)
	    sums=sums+sum
	    b=n-2
	    a=sums
	    #For HCF
	    if a<b:
	        x=b
	        b=a
	        a=x
	    while (a%b!=0):
	        d=a%b
	        a=b
	        b=d
	        
	    hcf=b
	    d1=sums/hcf
	    d2=(n-2)/hcf
	    print("%d/%d"%(d1,d2))
    
ob=Number()
ob.main()