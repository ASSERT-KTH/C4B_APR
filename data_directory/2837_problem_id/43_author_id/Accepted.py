def fun(n):
    ln = len(n)
    tmp = ord(n[0])
    tmp = tmp - 47
    for i in range(ln-1):
        tmp *=10
    print(tmp - int(n))
        

if __name__ == "__main__":
    n = input()
    fun(n)