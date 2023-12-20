f = open("D:/ege/17.txt")
a = [int(s) for s in f]
a_sp = [x for x in a if str(x)[-1] == str(x)[-2]]
count =0
max_sum=0
for i in range(1, len(a)):
    first = a[i - 1]
    second = a[i]
    if (abs(first) % 10 == abs(second) // 10 % 10) or (abs(second) % 10 == abs(first) // 10 % 10):
        if (first % 7 == 0) != (second % 7 == 0):
            if first**2 + second**2 <= min(a_sp)**2:
                count+=1
                max_sum = max(max_sum, first**2 + second**2)
print(count, max_sum)