#Justin Hershberger
#Py3.5

import fileinput

if __name__ == '__main__':
    num_args = 2
    for i in range(num_args):
        if i == 0:
            h,m = input().split(':')
        else:
            a = int(input())

    temp_h = 0
    temp_m = 0

    temp_m = a + int(m)
    # print(temp_m)
    if(temp_m > 59):
        temp_h = temp_m // 60
        temp_m -= (60 * temp_h)
        # print(temp_m)
    if(temp_h + int(h) > 23):
        temp_h = (temp_h + int(h)) - 24
        # print(temp_h)
    else:
        temp_h += int(h)

    if(temp_h < 10):
        if(temp_m < 10):
            final = '0'+str(temp_h) + ':0' + str(temp_m)
        else:
            final = '0'+str(temp_h) + ':' + str(temp_m)
    else:
        if(temp_m < 10):
            final = str(temp_h) + ':0' + str(temp_m)
        else:
            final = str(temp_h) + ':' + str(temp_m)
    print(final)
    # print(h,m, a)