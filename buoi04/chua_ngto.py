n = int(input("enter a number: "))
is_prime = True


# for i in range(2, n):
#     if n% i == 0:                 #cach 01
#         is_prime = False
#         break

i = 2
while i <= (n ** 0.5):
    if n%i == 0:                    #cach khac
        is_prime = False
        break
    i += 1

if is_prime == True:
    print(n, "la so ngto")
else:
    print(n, "khong phai so ngto")
