a = int(input())
b = int(input())
mid = 0
cout = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        mid += i
        cout += 1

mid = mid / cout

print(mid)

