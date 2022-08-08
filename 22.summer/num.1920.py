n = int(input())
numList = [int(x) for x in input().split(" ")]
m = int(input())
checkList = [int(x) for x in input().split(" ")]

"""
시간초과된 코드
for i in checkList:
    if i in numList:
        print("1")
    else:
        print("0")
"""
def binary(target):
    left = 0
    right = n-1
    while left<=right:
        mid = (left+right)//2
        if numList[mid] == target: return True
        elif target<numList[mid]:
            right = mid-1
        else:
            left = mid + 1
    return False

for i in checkList:
    if binary(i): print("1")
    else: print("0")
