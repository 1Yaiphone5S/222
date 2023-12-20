for i in range(100, 150):
    a="0"+"1"*i+"2"*i+"0"
    while not("00" in a):
        a = a.replace("02", "101")
        a = a.replace("11", "2")
        a = a.replace("12", "21")
        a = a.replace("010", "00")
    def sum_of_digits(num):
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum
    c=sum_of_digits(int(a))
    k = 0
    for n in range(2, c // 2 + 1):
        if (c % n == 0):
            k = k + 1
    if (k <= 0):
        print(i)
        break
