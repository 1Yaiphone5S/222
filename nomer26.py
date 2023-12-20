f=open("D:/ege/26-1.txt")
a = [int(z) for z in f]
a.sort()
k=0
maxx=0
m=[]
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]%2!=0 and a[j]%2!=0:
           m.append((a[i]+a[j])//2)
m.sort()
for i in range(len(m)):
    if m[i] in a:
        k+=1
        maxx=max(maxx, m[i])

print(k, maxx)
