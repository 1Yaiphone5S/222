import random
from random import randint

# Функия создаёт матрицу заданного размера случайным образом
def matrand(x, y):
    Z=[]
    for i in range(x):
        Z.append([])
        for j in range(y):
            Z[i].append(random.randint(-9, 9))
    return Z

# Функия для вывода матрицы
def printm(V):
    for i in range(len(V)):
        for j in range(len(V[i])):
            print("%4d" % V[i][j], end=' ')
        print()

# Функия для перемножения мариц по определению и нахождения количества элементарных операций
def matrumn(A, B):
    cs = 0
    cu = 0
    Z = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                Z[i][j] += A[i][k] * B[k][j]
                cu += 1
                if k > 0:
                    cs += 1
    if (len(A) * len(B) > 900 or (len(B) * len(B[0])) > 900):
        return "0", cu, cs
    else:
        return Z, cu, cs

# Функия, создающая нулевую матрицу размера n x n, для найденого n
def matrnull(n):
    Z=[]
    for i in range(n):
        Z.append([])
        for j in range(n):
            Z[i].append(0)
    return Z

# Функия, достраивабщая матрицу до размера n x n нулевыми строками и столбцами для алгоритма Штрассена
def matrdostr(X, n):
    D = matrnull(n)
    for i in range(len(X)):
        for j in range(len(X[0])):
            D[i][j]+=X[i][j]
    return D


# Ввод размеров двух матриц и параметра k
print("Введите размер матрицы A (m x n):")
m, n = map(int, input().split())
pr=n
print("Введите размер матрицы B (n x p):")
n, p = map(int, input().split())

# Проверка, что количество столбцов первой матрицы равно количеству строк второй
if n!=pr:
    print("Ошибка!\n"
          "Количество столбцов матрицы A и количество строк матрицы B должны совпадать.")
    exit()
print("Введите значение параметра k:")
k=int(input())


# Ввод матриц
print("Выберите способ ввода матрицы:\n"            
      "Чтобы выбрать ввод вручную введите: 1, чтобы сгенерировать случайным образом введите: 2")
ch=(int(input()))
if ch!=1 and ch!=2:
    print("!Такой комманды нет!\n")
    exit()
if ch == 1:
    print("Введите элементы матрицы A ({0} x {1}):".format(m, n))
    A = []
    for i in range(m):
        A.append(list(map(int, input().split())))
    print("Введите элементы матрицы B ({0} x {1}):".format(n, p))
    B = []
    for j in range(n):
        B.append(list(map(int, input().split())))
    if (len(A) * len(B) > 900 or (len(B) * len(B[0])) > 900):
        print("!Матрицы имеют слишком больой размер, их вывод будет отключён!\n")
    if (len(A)!=m or len(A[0])!=n) or (len(B)!=m or len(B[0])!=p):
        print("!Значения внутри матриц заданы неверно!\n")
        exit()
    else:
        print("Матрица А")
        printm(A)
        print("Матрица B")
        printm(B)
if ch == 2:
    A = matrand(m, n)
    B = matrand(n, p)
    print("Матрицы сгенерированы случайным образом.")
    if (len(A) * len(B) > 900 or (len(B) * len(B[0])) > 900):
        print("!Матрицы имеют слишком больой размер, их вывод будет отключён!\n")
    else:
        print("Матрица А")
        printm(A)
        print("Матрица B")
        printm(B)


# Вывод умножения мартиц по определению
C, cu,cs = matrumn(A, B)
print("Произведение матриц по определению")
if C=="0":
    print("!Матрица имеет слишком больой размер, её вывод будет отключён!\n")
else:
    printm(C)
print("Число элементарных операций умножения")
print(cu)
print("Число элементарных операций сложения")
print(cs)

# Вычисление n, которое требуется для алгоритма Штрассена
for x in range(n, n+100):
    y=x
    while y>k and y%2==0:
        y=y//2
    if y<=k:
        break


# Матрицы достраиваются до размера n x n для алгоритма Штрассена
E=matrdostr(A, x)
F=matrdostr(B, x)