s = input()
res = s.count('VK')
s = s.replace('VK', '')
res += 'VV' in s or 'KK' in s
print(res)