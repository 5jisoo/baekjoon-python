
word = input()
cWord = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in cWord:
    word = word.replace(i, "*")
print(len(word))
