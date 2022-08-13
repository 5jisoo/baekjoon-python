def primeNumber(num):
    if num <= 1:
        return False
    elif num<=3:
        return True
    else:
        for i in range(2, num+1):
            if num%i==0:
                return False
            if i*i > num:
                break
        return True

m, n = map(int, input().split(" "))
for i in range(m, n+1):
    if primeNumber(i):
        print(i)
