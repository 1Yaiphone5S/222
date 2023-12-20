x=''
k=0
for a in range(2, 9, 2):
    for b in range(0,9):
        for c in range(0, 9):
            for d in range(0, 9):
                for e in range(0, 8):
                    x=str(a)+str(b)+str(c)+str(d)+str(e)
                    if x.count("3")<=1 and int(x[0])%2==0 and x[-1]!="1" and x[-1]!="8":
                        k+=1
print(k)