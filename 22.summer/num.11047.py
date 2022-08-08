"""
시간초과 코드

n, k = map(int, input().split(" "))
coinList = []
i=0
total = 0
while i<n:
    coin = int(input())
    coinList.append(coin)
    i += 1

for i in range(n-1,-1,-1):
    while k >= coinList[i]:
        k -= coinList[i]
        total +=1

print(total)
"""


# 불필요한 이중반복문 사용은 지양하자!!
n, k = map(int, input().split(" "))
coinList = []
i=0
total = 0
while i<n:
    coin = int(input())
    coinList.append(coin)
    i += 1

for i in range(n-1,-1,-1):
    total += k//coinList[i]
    k %= coinList[i]

print(total)


