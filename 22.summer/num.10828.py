import sys
input=sys.stdin.readline

n = int(input())
pointer = 0
stack = [0]*n
for i in range(n):
    command = input().strip().split(" ")
    if command[0] == "push":
        stack[pointer] = command[1]
        pointer+=1
    elif command[0] == "pop":
        if pointer==0: print("-1")
        else:
            pointer -=1
            print(stack[pointer])
    elif command[0] == "size":
        print(pointer)
    elif command[0] == "empty":
        if pointer != 0: print("0")
        else: print("1")
    elif command[0] == "top":
        if pointer == 0: print("-1")
        else: print(stack[pointer-1])
    
