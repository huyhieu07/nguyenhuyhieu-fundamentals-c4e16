name01 = "hieu007"
pass01 = "123"
countt = 0
while True:

    namee = input("usename: ")
    if namee == name01:
        pasz = input("password: ")
        if pasz == pass01:
            print("welcome, my king")
            break
        else:
            print("wrong password!!!")
            break
    else:
        print("go away!")
        # break
    countt += 1
    if countt == 3:
        print("you failed to login 3 times")
