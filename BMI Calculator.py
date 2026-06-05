#BMI Calculator
height =float(input("Enter your height in meter : "))
weight =float(input("Enter your weight in kg : "))
gender =input("What's your gender : ")
bmi = weight/(height**2)
if gender not in  ["male", "female"] :
    print("Mention your gender")
else :
    print(f"Your BMI is {round(bmi,2)}")
