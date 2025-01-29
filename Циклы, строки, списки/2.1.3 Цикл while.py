a = int(input())
b = int(input())
flag = False

if a > b:
    n = a
else:
    n = b

while not flag:
    if n % a == 0 and n % b == 0:
        print(n)
        flag = True
    else:
        n += 1
