f=open("D:/ege/24.txt").readline()
k=3
kmaxx=0
for i in range(len(f)-4):
    if f[i:i+4] != 'XZZY':
        k+=1
    else:
        k=3
    kmaxx=max(k, kmaxx)
print(kmaxx)
