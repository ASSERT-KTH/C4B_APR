import sys
sys.stdin = open("input2",'r')
string = input()
cnt = v = 0
s = ''
if (len(string) == 1):
    print('0')

elif (len(string) == 2):
    if('KV' in string):
        print('0')
    else:
        print('1')
else:
    for i in range(0,len(string)-1):
        if v == 1:
            v = 0
            continue
        if(string[i] == 'V' and string[i+1] == 'K'):
            cnt += 1
            v = 1
            s += '0'
        else:
            s += string[i]
            v = 0
        if(i == len(string)-2 ):
            s += string[len(string)-1]

    if('VV' in s or 'KK' in s):
        cnt += 1

    print(cnt)