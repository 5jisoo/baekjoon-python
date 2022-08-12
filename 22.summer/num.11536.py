n = int(input())
nameList = []
sortedNameList = []
for i in range(n):
    name = input()
    nameList.append(name)

sortedNameList = sorted(nameList)

if nameList == sortedNameList:
    print("INCREASING")
elif nameList == sorted(sortedNameList, reverse = True):
    print("DECREASING")
else:
    print("NEITHER")
