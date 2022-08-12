n = int(input())
square = 1
total = 0
cnt = 1
while n // square >= 10:
    square *=10
    cnt += 1

total += (n-square+1)*cnt

square //= 10
cnt -= 1

while cnt:
    total += (square * 9)*cnt
    cnt -=1
    square //= 10
print(total)
