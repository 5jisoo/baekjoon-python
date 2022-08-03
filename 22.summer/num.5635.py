stuNum = int(input())
youngStu = ""
youngdate = 00000000
oldStu = ""
olddate = 99999999
while stuNum:
    name, day, month, year = input().split(" ")
    day, month, year = int(day), int(month), int(year)
    date = year*10000 + month * 100 + day
    if date > youngdate:
        youngdate = date
        youngStu = name
    if date < olddate:
        olddate = date
        oldStu = name
    stuNum-=1
print(youngStu)
print(oldStu)
