def f(x, n):
    s=''
    while x>0:
        s = str(x%n) + s
        x//=n
    return s
for i in range(10, 100):
     if f(i, 8)[-1]=="0" and f(i, 9)[-1]=="0":
         print(i)
         break