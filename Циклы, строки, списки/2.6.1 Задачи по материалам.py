n = int(input())
list1 = []

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if len(list1) == n:
            break
        else:
            list1.append(i)

print(' '.join(map(str, list1)))
