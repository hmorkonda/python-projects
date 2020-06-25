

def primecheck(n):
    for i in range(1,n):
        if i >= 2:
            for i in range(2, n):
                if n%i != 0 or n%2 != 0:
                    print('not prime', i)
                    # break
            else:
                print('prime', i)
        else:
            print('not prime', i)


print(primecheck(10))



