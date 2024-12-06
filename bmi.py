def main():
    weight = float(input("Please, enter your height: "))
    heigh = int(input("Please, enter your weight: "))
    total_bmi = bmi(weight, heigh)
    print(total_bmi)
    


def bmi(x, y):
    total_bmi = round((x/(y * y)) * 703)

    if total_bmi >= 18 and total_bmi <= 25:
        return f"Your BMI is {total_bmi}\nYou are within the ideal weight range"
    else:
        return f"Your BMI is {total_bmi}\nYou are overweight. You should see your doctor"

    

main()

