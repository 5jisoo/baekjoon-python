"""
- 시간초과가 뜬 코드

cardNum = int(input())
cardList= [x for x in range (1, cardNum+1)]
while len(cardList)!=1:
    cardList.pop(0)
    firstCard = cardList.pop(0)
    cardList.append(firstCard)
print(cardList[0])
"""

cardNum = int(input())
square = 2
if cardNum ==1 or cardNum==2:
    print(cardNum)
else:
    while cardNum//square>1:
        square *= 2
        if square==cardNum:
            square//=2
            break
    print((cardNum-square)*2)





