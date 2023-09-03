vp = int(input())
vd = int(input())
t = int(input())
f = int(input())
c = int(input())
k = 0
p = 0
while True:
    p += vp*t #пока дракон ещё не стартовал
    if (p >= c): break #добежала до замка
    p *= vd/(vd-vp) #позция когда дракон догнал
    if (p >= c): break #добежала до замка    
    k += 1 #сбросила драгоценность
    t = f + p / vd #время до следующего старта дракона
print(k)