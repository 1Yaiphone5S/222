for n in range(1, 10**9):
    s=bin(n)[2:]
    s=str(s)

    if n%2==0:
        s+="01"
    else:
        s+="10"
    r=int(s,2)
    if r>102:
        print(r)
        break