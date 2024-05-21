elem = []

for i in ["Height", "Weight"]:
    text = f'Please enter {i}: '
    try:
        indicator = int(input(text))
    except ValueError:
        print(f"Only integers are allowed")

    elem.append(indicator)

def BMICalculator(weight, height):

    BMI_indicator = weight/height**2

    if BMI_indicator < 18.5:
        print("Underweight")
    elif BMI_indicator > 18.5 and BMI_indicator < 24.9:
        print("Normal")
    elif BMI_indicator > 24.9:
        print("Overweight")


BMICalculator(elem[0], elem[1])