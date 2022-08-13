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

n = int(input())
numList = [int(x) for x in input().split(" ")]
cnt = 0

for i in numList:
    if primeNumber(i):
        cnt+=1

print(cnt)