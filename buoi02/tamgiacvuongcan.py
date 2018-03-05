# for i in range(6):
#     for i in range(i+1):
#         print("* ", end="")
#     print()

for i in range(6):
    for j in range(6):
        if j >= 5 - i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
