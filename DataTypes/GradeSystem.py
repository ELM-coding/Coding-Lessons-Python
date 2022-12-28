#ask the user to enter marks and save in variable 'marks'
marks=int(input("Please Enter The Marks"))
#check if the marks is btwn 0 to 20
if marks>=0 and marks<20:
    print("FAIL")
elif marks>=20 and marks<40:
    print("PASS")
elif marks>=40 and marks<60:
    print("GOOD")
elif marks>=60 and marks<80:
    print("V.GOOD")
elif marks>=80 and marks<=100:
    print("EXCELLENT")
else:
    print("Incorrect value")