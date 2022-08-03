testcase = int(input())
while testcase:
    playerNum = int(input())
    bestPlayer = ""
    maxPrice = 0
    while playerNum:
        price, name = input().split(" ")
        price = int(price)
        if price > maxPrice:
            maxPrice = price
            bestPlayer = name
        playerNum-=1
    print(bestPlayer)
    testcase-=1
