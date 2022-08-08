a = int(input())
b = int(input())
c = int(input())
mul = a*b*c
numList = [0]*10
while mul:
    numList[mul%10] += 1
    mul //= 10
for i in numList:
    print(i)
