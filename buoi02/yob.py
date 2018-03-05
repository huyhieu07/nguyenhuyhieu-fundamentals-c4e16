yob = int(input("your year of birth?"))

age = 2018 - yob

print("your age:", age)

if age < 10:  #conditional statement  #bieu thuc dk
    print("baby")
    print("hi")

elif age <= 18:      #10 -18 tuoi
        print("teenager")

elif age ==24:      #so sanh gia tri chinh xac
    print("lay ck thoi")

else:                   #cai lelse nay ko co dk, cai con lai
    print("not baby")

print("bye")
