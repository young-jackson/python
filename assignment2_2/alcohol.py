def main():
    drinks = input("How many units of alcohol do you drink in a week?\n")
    gender = input("Enter your gender identity (1-3). 1. Male 2. Female 3. Other/Prefer not to say")
    if gender == 1:
        if int(drinks) <= 14:
            print("Your alcohol consumption is under the moderate-risk limit.")
        else:
            print("Your alcohol consumption is over the moderate-risk limit.")
    else:
        if int(drinks) <= 7:
            print("Your alcohol consumption is under the moderate-risk limit.")
        else:
            print("Your alcohol consumption is over the moderate-risk limit.")


main()

