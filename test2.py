def f(x, n):
    s=''
    while x>0:
        s=str(x%n)+s
        x=x//n
    return s
print(f(9, 9))