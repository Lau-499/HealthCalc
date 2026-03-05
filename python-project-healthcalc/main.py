from healthcalc.health_calc_impl import HealthCalcImpl

def main():
    calc = HealthCalcImpl()

    print("Welcome to your Health Calculator!")

    finish = False

    def ask_float(message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Value must be a number, try again.")

    while not finish:
        answer = input("Do you want to know your Body Mass Index? Y/N \n")

        while answer.upper() != "Y" and answer.upper() != "N":
            answer = input("Your answer must be 'Y' or 'N', try again: \n")

        if answer.upper() == "Y":
            weight = ask_float("Input your weight (kg): \n")
            height = ask_float("Input your height (m): \n")

            bmi = calc.bmi(weight, height)

            print("Your BMI is: ", bmi)
            print("According to that, your Health Status is: ", calc.bmi_classification(bmi))

        answer2 = input("Do you want to know your Ideal Body Weight? Y/N \n")

        while answer2.upper() != "Y" and answer2.upper() != "N":
            answer2 = input("Your answer must be 'Y' or 'N', try again: \n")

        if answer2.upper() == "Y":
            height = ask_float("Input your height (m): \n")
            sex = input("Input your sex ('M' for male or 'F' for female): \n")

            while sex.upper() != "M" and sex.upper() != "F":
                sex = input("Your sex must be either 'M' (male) or 'F' (female), try again: \n")

            ibw = calc.lorentz(sex.upper(), height)

            print("Your Ideal Body Weight is: ", ibw, " kg.")

        answer3 = input("Do you want to know your Waist-To-Hip Ratio? Y/N \n")

        while answer3.upper() != "Y" and answer3.upper() != "N":
            answer3 = input("Your answer must be 'Y' or 'N', try again: \n")

        if answer3.upper() == "Y":
            waist = ask_float("Input your waist perimeter (m): \n")
            hip = ask_float("Input your hip perimeter (m): \n")
            sex = input("Input your sex ('M' for male or 'F' for female): \n")

            while sex.upper() != "M" and sex.upper() != "F":
                sex = input("Your sex must be either 'M' (male) or 'F' (female), try again: \n")

            whr = calc.whr(waist, hip)

            print("Your Waist-to-Hip Ratio is: ", whr)
            print("According to that, your body morfology is: ", calc.whr_classification(sex, whr))

        answer4 = input("Are you finished using your Health Calculator? Y/N \n")

        while answer4.upper() != "Y" and answer4.upper() != "N":
            answer4 = input("Your answer must be 'Y' or 'N', try again: \n")
        
        if answer4.upper() == "Y":
            finish = True


if __name__ == "__main__":
    main()



        




            




