m = int(input())
n = int(input())

i=m
total = 0
minNum = n
find = 0

while i<=n :
    j=1
    while j*j<=i:
        if j*j==i:
            total+=i
            find = 1
            if i<minNum: minNum=i
            break
        else:
            j+=1
    i+=1
if(find):
    print(total)
    print(minNum)
else:
    print(-1);

