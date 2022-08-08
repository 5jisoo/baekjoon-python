n = int(input())
scoreList = []
firstPlayer = 0
maxScore = 0
for _ in range(n):
    maxScore = 0
    card = [int(x) for x in input().split(" ")]
    for i in range(5):
        for j in range(i+1,5):
            for k in range (j+1, 5):
                score = card[i] + card[j] + card[k]
                score %= 10
                if score >= maxScore:
                    maxScore = score
    scoreList.append(maxScore)

for i in range(n):
    if scoreList[i] >= maxScore:
        maxScore = scoreList[i]
        firstPlayer = i+1

print(firstPlayer)


