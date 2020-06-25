n = int(input('enter n: '))
num = 1

for i in range(1, n+1):
    for j in range(0,i):
        print(num, end=' ')
        num = num+1

    print()


