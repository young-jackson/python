def main():
    size = int(input("Enter the number of the participants.\n"))
    while size <= 1:
        print("The number must be at least 2!")
        size = int(input("Enter the number of the participants.\n"))

    participants = []
    total = 0

    for i in range(size):
        cost = float(input(f"Enter the sum (eur) paid by participant no {i + 1}.\n"))
        participants.append(cost)
        total += cost
    print(f"Total costs are {total:.2f} eur.")

    price = total / size

    for i in range(size):
        if participants[i] >= price:
            print(f"Participant no {i + 1} should receive {participants[i] - price:0.2f} eur.")
        else:
            print(f"Participant no {i + 1} should pay {price - participants[i]:0.2f} eur.")


main()
