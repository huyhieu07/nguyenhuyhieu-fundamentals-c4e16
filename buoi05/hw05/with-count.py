menu = [1 ,6 ,8 ,1 ,2 ,1 ,5 ,8 ]
countt = 0
n = int(input("enter a number: "))

for i in range(len(menu)):
    if n == menu[i]:
        countt +=1

if countt < 2:
    print(n, "appears",countt,"time in my list")
else:
    print(n, "appears",countt,"times in my list")
