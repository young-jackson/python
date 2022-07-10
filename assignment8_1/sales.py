def main():
    filename = input("Enter a filename:\n")
    sales = {}
    try:
        file = open(filename, "r")
        for row in file:
            row = row.rstrip()
            parts = row.split(":")
            if len(parts) != 2:
                print("Invalid line:", row)
            else:
                employee = parts[0]
                try:
                    sale = float(parts[1])
                    if employee not in sales or sales[employee] < sale:
                        sales[employee] = sale
                except ValueError:
                    print("Invalid sale:", parts[1])
        file.close()

        # Print the best sale of each employee
        if sales == {}:
            print("The file did not contain any correct sales.")
        else:
            print("The best sale of each employee:")
            print("Employee          Sale (eur)")
            print("----------------------------")
            employees = sorted(sales)
            for employee in employees:
                print(f"{employee:18s}{sales[employee]:>10.2f}")
    except OSError:
        print("Error in reading file {:s}. Closing program.".format(filename))


main()
