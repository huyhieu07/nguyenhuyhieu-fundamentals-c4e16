s = input("enter: ")
#strip cup spaces at start/ end of string
words = s.strip().splip(" ")
numbers = []

for words in words:
    numbers.aapend(int(words))

is_sorted = True

for i in range(len(numbers)-1):
    if numbers[i] > numbers [i +1]:
        is_sorted = False
        break

if is_sorted:
    print("your sequence is already sorted")
else:
    print("your sequence is not sorted yet")

sorted_list = []

while True:

    min_numb = min(numbers)
    sorted_list.append(min_numb)
    numbers.remove(min_numb)

    if len(numbers) == 0:
        break
print(*sorted_list)
    
