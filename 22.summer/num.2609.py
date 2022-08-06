num1, num2 = map(int, input().split(" "))

def gcd(num1, num2):
    if num2>num1: num2,num1 = num1,num2
    if num2 == 0: return num1
    else: gcd(num2, num1%num2)

def lcm(num1, num2):
    return num1*num2/gcd(num1, num2)

numGCD = gcd(num1, num2)
numLCM = lcm(num1, num2)
