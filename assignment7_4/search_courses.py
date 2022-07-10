def func1():
    pass


def func2():
    pass


def func3():
    pass


def main():
    filename = input("Enter the name of the file.\n")
    cont = True
    try:
        file = open(filename)
        file.readline()
        print("Enter search criterion or skip by pressing enter.")
    except OSError:
        print(f"Error in reading file {filename}. Closing program.")
        cont = False
    while cont:
        code = input("Code: ")
        name = input("Name: ")
        cred = input("Credits: ")
        period = input("Period(s): ")
        level = input("Level (Bachelor/Master): ")
        print("\nCode        Name                                         ECTS Period Level  "
              "\n-----------------------------------------------------------------------------")
        for line in file:
            components = line.rstrip().split(",")
            if len(components) == 5:
                if code.lower() in components[0].lower() and name.lower() in components[1].lower():
                    if (cred == components[2] or cred == "") and (period == components[3] or period == "") and (level == components[4] or level == ""):
                        print(f"{components[0]:12s}{components[1]:45s}{components[2]:5s}"
                              f"{components[3]:7s}{components[4]:7s}")

        prompt = input("\nDo you want to do a new search? Enter yes or no.\n")
        if prompt == "no":
            cont = False
        else:
            file = open(filename)
            file.readline()


main()
