def main():
    amount = int(input("How many products are you going to input?\n"))
    prices = [0.0] * amount
    for i in range(amount):
        inputted_price = float(input("Enter the price of the next product (eur).\n"))
        prices[i] = inputted_price

    print("Discount prices")

    sum = 0
    for x in prices:
        if x >= 50:
            print(f"{0.7 * x:0.2f} eur")
            sum += 0.7 * x
        else:
            print(f"{0.9 * x:0.2f} eur")
            sum += 0.9 * x

    print(f"Sum of discount prices: {sum:0.2f} eur.")



main()
