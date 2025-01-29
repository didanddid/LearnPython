a = [int(i) for i in input().split()]
b = []
str1 = ''
a.sort()

for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            continue
        if a[i] == a[j]:
            if a[j] not in b:
                b.append(a[j])
str1 = ' '.join(map(str, b))
print(str1)