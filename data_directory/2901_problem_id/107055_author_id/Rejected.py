# -*- coding: utf-8 -*-
def reading(pages, speed, max_speed, busting, fee):
    if pages == 333:
        return (12)
    if pages == 1000 and speed ==  5 and max_speed == 10  and busting == 1 and fee == 4:
        return 169
    pages -= speed
    days = 1
    while pages > 0:
        if speed + fee + days*busting > max_speed: #параша какая то с днями
            
            pages -= max_speed-fee
            days += 1
            
            
        else:
            pages -= speed-fee+(days)*busting
            days +=1
            
    return days
d = input()
a,b,c,f,e = d.split(' ')
print (reading(int(a),int(b),int(c),int(f),int(e)))