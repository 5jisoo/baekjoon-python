num1, num2 = map(int,input().split(" "))
def changeNum(num):
    a = num//100
    b = num%100//10
    c = num%10
    return c*100 + b*10 + a
num1 = changeNum(num1)
num2 = changeNum(num2)
if num1>=num2:
    print(num1)
else:
    print(num2)
