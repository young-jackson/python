def main():
    name = input("Enter the name of the file containing the birthdays:\n")
    try:
        textfile = open(name)
        month = input("Enter a month as an integer between 1 and 12:\n")
        print("Birthday Name")
        count = 0
        for line in textfile:
            line2 = line.rstrip().split(".")
            if line2[1] == month and float(line2[0]) <= 31:
                line3 = line2[0] + "." + line2[1] + "."
                print(f"{line3:8s} {line2[2]}")
                count += 1
        if count != 0:
            print(f"\nThe file contains birthdays of {count} people in this month.")
        else:
            print("There are no birthdays in this month in the file.")

    except OSError:
        print(f"Error in reading the file '{name}'. Program ends.")
    except ValueError:
        print(f"Incorrect date in the file '{name}'. Program ends.")


main()
