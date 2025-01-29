a = int(input())
b = int(input())
c = int(input())
d = int(input())
string = ''

for j in range(c,d+1):
    string += '\t' + str(j)
print(string)

for i in range(a,b+1):
    string = str(i) + '\t'
    for j in range(c,d+1):
        string += str(i*j) + '\t'
    print(string)
