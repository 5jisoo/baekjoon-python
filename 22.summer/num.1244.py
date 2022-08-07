numSwitch = int(input())
switchList = [int(x) for x in input().split(" ")]
numStudent = int(input())
while numStudent:
    gender, num = map(int, input().split(" "))
    if gender == 1:
        for i in range (1,numSwitch+1):
            if i%num==0:
                switchList[i-1] = int(not switchList[i-1])
    else:
        switchList[num-1] = int(not switchList[num-1])
        left = num-2
        right = num
        while left>=0 and right <= numSwitch-1:
            if switchList[left]==switchList[right]:
                switchList[left] = int(not switchList[left])
                switchList[right] = int(not switchList[right])
            else: break
            left -= 1
            right += 1
    numStudent -= 1

for i in range(numSwitch):
    print(switchList[i], end=" ")
    if (i+1)%20 ==0: print("")
