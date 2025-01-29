lst = [int(i) for i in input().split()]
x = int(input())
res = []
for j in range(len(lst)):
    if x == lst[j]:
        res.append(j)

if len(res) == 0:
    print('Отсутствует')
else:
    print(' '.join(map(str, res)))