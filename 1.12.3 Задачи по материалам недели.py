import math

pi = 3.14
typeRoom = str(input())

if typeRoom == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = float(math.sqrt(p * (p - a) * (p - b) * (p - c))) # формула Герона - определение площади треугольника сторонам
    print(S)
elif typeRoom == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = float(a * b)
    print(S)
elif typeRoom == 'круг':
    a = int(input())
    S = float(pi * (a ** 2))
    print(S)