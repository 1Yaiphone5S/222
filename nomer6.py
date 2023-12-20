for x in range(10,1000 +1):
    b=str(bin(x)[2:])
    b=b[1:]
    for i in b:
        if i == "0":
            b=b[1:]
        if i =="1":
            break
        if b == "":
            b=0
    b = int(str(b), 2)
    print(x-b)
