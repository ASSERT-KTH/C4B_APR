def check_symbols(_str, _arr):
    _res = False
    for x in _str:
        for y in _arr:
            if x == y:
                _res = True
    return _res

_str = input()
_arr = ['H', 'Q', '9', '+']

if check_symbols(_str, _arr):
    print('YES')
else:
    print('NO')