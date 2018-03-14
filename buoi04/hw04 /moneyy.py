n = str(int(input("nhap so tien cua ban: ")))
moneyy = list(n)    #cat thanh chuoi 123456...


for i in range(len(moneyy)-3, 0, -3):
    moneyy.insert(i, ',')

print("so tien cua ban: $", *moneyy, sep='')
