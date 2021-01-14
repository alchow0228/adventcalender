data = open("C:/users/cala/Documents/pwords.txt")
list = data.readlines()
i = 0
item2 = 0
item3 = 0
for i in list:
    item1 = i
    total = item1+item2+item3
    for x in list:
        item2 = x
        total = item1+item2+item3
        for y in list:
            item3 = y
            total = item1+item2+item3
            if total == 2020:
                print(total)
                print(item1*item2*item3)
                print(item1)
                print(item2)
                print(item3)
