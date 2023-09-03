s = input()

if len(s) > 0 and len(s) < 101:
    if s.find('h') != -1:
        h1 = s.find('h')
        if s.find('e',h1) != -1:
            e1 = s.find('e',h1)
            if s.find('l', e1) != -1:
                l1 = s.find('l',e1)
                if s.find('l', l1+1) != -1:
                    l2 = s.find('l',l1)
                    if s.find('o', l2) != -1:
                        print('YES')
                    else:
                        print('NO')
                else:
                    print('NO')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')