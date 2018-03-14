favs = ["teaching", "films", "games"]
for index, fav in enumerate(favs):
    print(index +1, ". ", fav, sep='')

positionn = int(input("vi tri thay the: "))
print(favs[positionn-1])
neww = input("thay the bang: ")
favs[positionn-1] = neww
for index, favs in enumerate(favs):
    print(index + 1, ". ", favs, sep='')
