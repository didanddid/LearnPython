a = []
b = 0
flag = True
while flag:
    b = int(input())
    a.append(b)
    if sum(a) == 0:
        flag = False
        b = 0


for i in range(len(a)):
    a[i] *= a[i]
    b += a[i]

print(b)

