def main():
    try:
        file = open(input("Enter the name of the file containing the recipe:\n"))
        name = file.readline().rstrip()
        amount = int(file.readline().split()[0])
        print(f"This recipe of {name} makes {amount} servings.")
        valid = False
        while not valid:
            servings = input("How many servings do you want to make with this recipe?\n")
            try:
                servings = int(servings)
                valid = True
            except ValueError:
                print("The amount needs to be an integer!")
            if valid and servings <= 0:
                print("The amount needs to be positive!")
                valid = False
        print(f"\nFor {servings} servings of {name} you will need:")
        file.readline()
        for line in file:
            try:
                splitLine = line.rstrip().split(" ", 1)
                x = float(splitLine[0]) / amount * float(servings)
                print(f"{x:0.1f} {splitLine[1]}")
            except ValueError:
                print(line)
    except OSError:
        print("File could not be read. Terminating program")


main()
