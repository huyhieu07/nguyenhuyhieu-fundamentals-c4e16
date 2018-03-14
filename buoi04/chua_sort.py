numbers = [-10, -2018, 1, 0, -5, 7, 22, -20]

sorted_list = []

while True:

    min_numb = min(numbers)
    sorted_list.append(min_numb)
    numbers.remove(min_numb)

    if len(numbers) == 0:
        break
print(*sorted_list)        
