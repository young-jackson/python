def calculate_storage_size(battery_orders_weight):
    print(f"Required storage size is {battery_orders_weight / 150 * 10} cubic meters.")


def calculate_emissions(storage_size):
    print(f"Emissions in two weeks are {0.010 * (storage_size * 200)} CO2 equivalents.")


def main():
    print("Please choose one of the options")
    print("1 - Calculate storage size")
    print("2 - Calculate emissions")
    func = input()

    while func != "1" and func != "2":
        print("Please choose one of the options")
        print("1 - Calculate storage size")
        print("2 - Calculate emissions")
        func = input()

    if func == "1":
        size = input("How many kilograms of batteries are being supplied each two weeks?\n")
        calculate_storage_size(int(size))

    elif func == "2":
        size = input("What is the current storage size (cubic meters)?\n")
        calculate_emissions(int(size))


main()
