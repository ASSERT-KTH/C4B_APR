a=input()
print(['YES','NO'][all(len(set(a[i-7:i]))>1 for i in range(7,len(a)+1))])