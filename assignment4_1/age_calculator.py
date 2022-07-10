def calculate(name, age):
    if age < 18:
        print(f"{name}, you'll be eighteen in {18 - age} years.")
    elif age > 18:
        print(f"{name}, you turned eighteen {age - 18} years ago")
    else:
        print(f"{name}, you probably know you are exactly 18 years old?")


def main():
    my_name = input("What is your name?\n")
    my_age = int(input("What is your age in years?\n"))
    calculate(my_name, my_age)


main()
