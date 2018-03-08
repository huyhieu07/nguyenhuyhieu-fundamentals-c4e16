n = int(input('nhap 1 so: '))
k = 1
for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        k = i * j
        print(k  , end='  ')
    print()
