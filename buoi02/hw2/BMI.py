hee = int(input("your height(in cm): "))
wee = int(input("your weight( in kg): "))
bmi =  (wee/ ( hee * hee ))*10000
print("your bmi: ",bmi)
if bmi < 16:
    print("Severely underweight!!!")
elif bmi < 18.5:
    print("Underweight!")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight :)))")
else:
    print("wtf???")            
