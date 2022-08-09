n, k = map(int, input().split(" "))
if n-k >= (k-1)*k//2:
    left = (n - k) - ((k-1)*k//2)
    left%=k
    if left ==0:
        print(k-1)
    else:
        print(k)
else: print(-1)
