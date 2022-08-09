n, newScore, p = map(int, input().split(" "))
if n==0:
    print("1")
else: 
    scoreList = [int(x) for x in input().split(" ")]
    rank = -1
    if n==p and scoreList[-1] >= newScore:
        print(-1)
    else: 
        rank = n + 1
        for i in range(n):
            if newScore >= scoreList[i]:
                rank = i+1
                break
        print(rank)
