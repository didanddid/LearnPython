a = int(input())
if not(a % 4) and a % 100:
    print('Високосный')
elif not(a % 400):
    print('Високосный')
else:
    print('Обычный')