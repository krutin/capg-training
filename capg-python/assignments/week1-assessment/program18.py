def calc_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "underweight"
    elif 18.5 <= bmi < 24.9:
        category = "normal"
    elif 25 <= bmi < 29.9:
        category = "overweight"
    else:
        category = "obese"
    return bmi, category

weight = float(input("Enter weight in kg:"))
height = float(input("Enter height in meters:"))
bmi, category = calc_bmi(weight, height)
print("BMI: {}, Category: {}".format(bmi, category))