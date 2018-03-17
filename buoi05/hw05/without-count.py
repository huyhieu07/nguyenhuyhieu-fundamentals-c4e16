menu = [1 ,6 ,8 ,1 ,2 ,1 ,5 ,8 ]

n = int(input("enter a number: "))
k = []
for i in range(len(menu)-1):
    if menu[i] == n:
        k.append(n)

if len(k) < 2:
    print(n, "appears",len(k),"time in my list")
else:
    print(n, "appears",len(k),"times in my list")
