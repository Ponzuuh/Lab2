def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print("BMI is " + str(round(bmi, 2)))

    if (bmi<18.5):
        print("You are under weight")
    elif  (bmi>=18.5 and bmi<=25.0):
        print("Normal weight")
    else:
        print("You are over weight")


calculate_bmi(weight=57,height=1.73)