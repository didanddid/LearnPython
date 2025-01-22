a = int(input())
b = a % 10
c = a // 10

if c == 1 or c == 11 or c == 111:
    print(a, 'программистов')
else:
    if b == 0 or 5 <= b <= 9:
        print(a, 'программистов')
    elif b == 1:
        print(a, 'программист')
    elif 2 <= b <= 4:
        print(a, 'программиста')


