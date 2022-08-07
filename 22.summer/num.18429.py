def checkLoss(numkits):
    global total, cnt
    if numkits==0:
        cnt += 1
    else:
        for i in range(numKits):
            if visitCheck[i]==0:
                if total+kitList[i] < 500: continue
                else: 
                    visitCheck[i]=1
                    total+=kitList[i]
                    checkLoss(numkits-1)
                    total-=kitList[i]
                    visitCheck[i]=0

numKits, loss = map(int, input().split(" "))
kitList = [int(x)-loss for x in input().split(" ")]
total = 500
cnt = 0
visitCheck = [0]*numKits
checkLoss(numKits)
print(cnt)



