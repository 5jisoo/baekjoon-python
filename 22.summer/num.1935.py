def calculate(a, b, cal):
    if cal == "+": return a+b
    elif cal == "-": return a-b
    elif cal == "/": return a/b
    elif cal == "*": return a*b


n = int(input())
notation = list(input())
stack=[]
standard = 'A'
while n:
    num = input()
    for i in range(len(notation)):
        if notation[i]==standard:
            notation[i] = num
    standard = chr(ord(standard)+1)
    n-=1
for i in notation:
    if i.isdigit():
        stack.append(i)
    else:
        b = float(stack.pop())
        a = float(stack.pop())
        result = calculate(a,b,i)
        stack.append(result)
print("%.2f" %stack[0])