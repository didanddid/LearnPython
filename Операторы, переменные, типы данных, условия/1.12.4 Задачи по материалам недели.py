a = int(input())
b = int(input())
c = int(input())

# максимальное
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)

# Минимальное
if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
elif c <= a and c <= b:
    print(c)

# Среднее
if b <= a <= c or c <= a <= b:
    print(a)
elif a <= b <= c or c <= b <= a:
    print(b)
elif a <= c <= b or b <= c <= a:
    print(c)