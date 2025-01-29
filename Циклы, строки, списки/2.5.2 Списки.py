a = [int(i) for i in input().split()]
b = '' #[0 for i in range(len(a))]

for i in range(len(a)):
    if len(a) == 1:
        b += str(a[0])
    elif i < len(a) - 1:
        b = b + str(a[i - 1] + a[i + 1]) + ' '
    else:
        b = b + str(a[i - 1] + a[0])+ ' '
print(b)



