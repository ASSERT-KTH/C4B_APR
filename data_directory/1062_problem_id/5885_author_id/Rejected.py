def lucky(n):
    if int(n) > 7:return lucky(str(n.count('4')+n.count('7')))
    else: return 'YES' if n=='4' or n=='7' else 'NO'
print(lucky(input()))