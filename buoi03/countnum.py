numb = int(input("enter a number: "))

count = 0
while True:
    numb = numb // 10
    count += 1
    if numb == 0:
        break
print(count)
