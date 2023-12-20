def cc(x):
    s = ''
    while x != 0:
        s += str(x % 3)
        x //= 2
        return s[::-1]
print(cc(10))