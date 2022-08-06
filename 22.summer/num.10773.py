k = int(input())
numList = []
while k:
    num = int(input())
    if num!=0:
        numList.append(num)
    else:
        numList.pop(-1)
    k-=1
total = 0
for i in numList:
    total += i
print(total)
