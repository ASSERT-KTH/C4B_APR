#!usr/bin/python 3

def main():
    a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
    harm=[a,b,c,d]
    nums=set(range(1,e+1))
    nums2=set(range(1,e+1))
    for x in range(0,4):
        for y in nums2:
            if y%harm[x]==0:
                if y in nums:
                    nums.remove(y)
    print(e-len(nums))
    
if __name__=='__main__':
    main()