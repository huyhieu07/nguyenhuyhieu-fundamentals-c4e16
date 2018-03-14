print("guess your number game")
print("now think of a number from 0 to 100, then press C(chuan)/N(nho hon)/L( lon hon)")
print("* " * 20)    #gia su nguoi dung chon so 71

loww = 0
highh = 100

while True:
    midd = (loww + hightt) // 2
    ann = input("is {0} is your number? ".format(midd).lower()
    if ann == "c":
        print("chuan luon")
        break
    elif ann == "l":
        highh = midd
    elif ann == "l":
        loww = midd
       
