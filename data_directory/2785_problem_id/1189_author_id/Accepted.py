s = input()
res = s.count('VK')
s = s.split('VK')
res += sum(['VV' in x or 'KK' in x for x in s]) > 0
print(res)