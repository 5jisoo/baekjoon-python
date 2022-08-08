word = list(input())
length = len(word)
temp = []
wordList = []

for i in range(1,length-1):
    for j in range(i+1,length):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        temp.append(a+b+c)

for j in temp:
    wordList.append("".join(j))

wordList.sort()
print(wordList[0])
