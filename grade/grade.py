print("Welcome to the Grade Checker!")
marks = int(input("Enter Marks: "))

if marks >= 80:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
elif marks >= 40:
    print("C Grade")
else:
    print("Fail")
    