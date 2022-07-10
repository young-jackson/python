def main():
    length = float(input("How long is the route (km)?\n"))
    passengers = int(input("How many passengers?\n"))
    tariff = int(input("Enter the tariff period (1-2). 1. Weekday 6:00-18:00 2. Sunday, "
                       "official holiday or evening 18:00-6:00\n"))
    if passengers <= 4:
        if tariff == 1:
            cost = length * 0.99 + 4.90 + length / 55 * 60 * 0.89
        else:
            cost = length * 1.09 + 6.90 + length / 55 * 60 * 0.99
    else:
        cost = length * 1.59 + 6.90 + length / 55 * 60 * 0.99

    if passengers > 8:
        print(passengers, "passengers do not fit in one taxi.")
    else:
        print("The estimated taxi fare is", cost, "eur.")


main()

