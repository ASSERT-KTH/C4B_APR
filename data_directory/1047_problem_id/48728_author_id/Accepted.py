hh,mm = input().split(':')
hours = str(int(hh[1])+1)+hh[0]
if  hh<='05' and mm<=str(int(hh[1]))+hh[0] and hh>'00':
    print(hh+':'+hh[::-1])
elif hh<='05':
    
    print(hh[0]+str(int(hh[1])+1)+':'+hours)
elif hh<='09' or (hh=='10' and mm=='00'):
    print('10:01')

elif hh<='14'and mm<str(int(hh[1]))+hh[0]:
    print(hh+':'+hh[::-1])
elif hh<='14':
    print(hh[0]+str(int(hh[1])+1)+':'+hours)
elif hh<='19' or (hh=='20' and mm<='01'):
    print('20:02')
elif (hh=='20' and mm>='02') or (hh=='21' and mm<'12'):
    print('21:12')
elif (hh=='21' and mm>='12') or (hh=='22' and mm<'22'):
    print('22:22')
elif (hh=='22' and mm>='22') or (hh=='23' and mm<'32'):
    print('23:32')
elif (hh=='00' and mm=='00'):
    print('01:10')
else:
    print('00:00')