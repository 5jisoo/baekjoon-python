numClass = int(input())
testList = [int(x) for x in input().split(" ")]
supt, deSupt = map(int, input().split(" "))
total = 0
#이중반복문사용 -> 시간초과가 뜸. 주의하자 ,,
for i in testList:
    i -= supt
    total += 1
    if i>0:
        total += i//deSupt
        if i%deSupt!=0: total += 1
print(total)
