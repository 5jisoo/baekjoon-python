nowHr, nowMin, nowSec = map(int,input().split(":"))
startHr, startMin, startSec = map(int,input().split(":"))

if nowHr > startHr: startHr += 24

nowTime = nowSec + nowMin*60+ nowHr*3600
startTime = startSec + startMin*60 + startHr*3600

leftTime = startTime - nowTime

leftHr = leftTime/3600
leftTime %= 3600
leftMin = leftTime / 60
leftTime %= 60
leftSec = leftTime

print("%02d:%02d:%02d" %(leftHr, leftMin, leftSec))

