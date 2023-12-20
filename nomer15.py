def ddel(n, m):
    return n%m==0

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not(ddel(x, 17)<=(not(ddel(x, 53))) or a>=(90000000-x)):
            flag = False
            break
    if flag:
         print(a)

