for i in range(100, 150):
    a="0"+"1"*i+"2"*i+"0"
    while not("00" in a):
        a = a.replace("02", "101")
        a = a.replace("11", "2")
        a = a.replace("12", "21")
        a = a.replace("010", "00")
    c=0
    for x in range(len(a)):
        c += int(a[x])
    k = 0
    for n in range(2, c // 2 + 1):
        if (c % n == 0):
            k += 1
    if (k <= 0):
        print(i)
        break
