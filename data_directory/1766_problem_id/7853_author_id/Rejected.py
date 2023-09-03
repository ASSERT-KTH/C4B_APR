def solution():
    
    string = input()
    res = -1
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            tmp = 0
            buf = string[i:j]
            for k in range(len(string) - len(buf)):
                if buf == string[k:k + len(buf)]: tmp += 1
            if tmp > 1: res = max(res, len(buf))
    
    return res + 1

print(solution(), end= "")