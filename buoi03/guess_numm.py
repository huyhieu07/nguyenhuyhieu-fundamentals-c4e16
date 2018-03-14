from random import randint
# n = (randint(0, 100))
n = 43

playy = True
countt = 0
while playy:        #mac dinh ntn la dung luon
    numm = int(input("guess my number (0-100): "))

    if numm == n:
        print("chuan luon")
        # playy = False
        break
    elif numm > n:
        print("lon qua!")

    else:
        print("nho hon co!")
    countt += 1
    if countt == 7:
        print("ban thua roi :))")
        # playy = False
        break           #break la dung luon, kqt anything
