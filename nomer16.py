def F(a, b):
    if b==0:
        return a
    if a >= b > 0:
        return F(a-b, b)
    if a < b:
        return F(b, a)
k=0
for n in range(123456798, 1234567885 +1):
    if n % 5 !=0 and n%3!=0:
        k += 1
print(k)