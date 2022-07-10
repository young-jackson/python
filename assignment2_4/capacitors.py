def main():
    amount = int(input("How many capacitors are there?\n"))
    while amount <= 0:
        print("Enter a positive value!")
        amount = int(input("How many capacitors are there?\n"))
    connection = int(input("Are the capacitors connected:\n1. in series\n2. in parallel?\n"))
    
    while connection != 1 and connection != 2:
        print("Invalid choice!")
        connection = int(input("Are the capacitors connected:\n1. in series\n2. in parallel?\n"))
    i = 0
    capacitance = 0

    if connection == 2:
        while i < amount:
            capacitor = float(input("Enter the capacitance for the next capacitor:"))
            capacitance += capacitor
            i += 1
        c = capacitance
    else:
        while i < amount:
            capacitor = float(input("Enter the capacitance for the next capacitor:"))
            capacitance += 1 / capacitor
            i += 1
        c = 1 / capacitance
    print("The total capacitance of the capacitors is", c, "F.")


main()

