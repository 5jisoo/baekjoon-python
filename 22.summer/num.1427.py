num = int(input())
numList=[]
while num:
    numList.append(num%10)
    print(num%10, "넣음")
    num//=10
for i in range (len(numList)-1):
    maxIndex = i
    for j in range (i+1, len(numList)):
        if numList[j] > numList[maxIndex]:
            maxIndex = j
    numList[maxIndex], numList[i] = numList[i], numList[maxIndex]
for i in numList:
    print(i,end="")
