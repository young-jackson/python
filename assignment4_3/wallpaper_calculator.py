import math


def calculate_number_of_wallpaper_rolls(room_total_width, room_height):
    coefficient = math.floor(1005 / room_height)
    total = math.ceil(room_total_width / 53 / coefficient)
    return total


def calculate_price(number_of_rolls, price_per_roll):
    return number_of_rolls * price_per_roll


def main():
    cost = float(input("How much does a roll of wallpaper cost (in euros)?\n"))
    rooms = int(input("How many rooms do you need to paper?\n"))
    totalrolls = 0
    for i in range(rooms):
        print(f"{i + 1}. room")
        height = float(input("Enter the height of the room in cm:\n"))
        totalwidth = 0
        for k in range(4):
            totalwidth += float(input(f"Enter the width of the {k + 1}. wall in cm:\n"))
        totalrolls += calculate_number_of_wallpaper_rolls(totalwidth, height)

    print(f"You need to buy {totalrolls} wallpaper rolls.")
    print(f"The total cost is {calculate_price(totalrolls, cost):.2f} euros.")


main()
