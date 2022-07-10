def convert(amount, exchange_to, currency_dict):
    if exchange_to in currency_dict:
        return amount * currency_dict[exchange_to]
    else:
        return -1

def main():
    file_name = input("Enter the name of the file.\n")
    try:
        file = open(file_name)
        currency_dictionary = {}
        for row in file:
            parts = row.split(",")
            if len(parts) == 3:
                try:
                    currency_dictionary[parts[0]] = float(parts[2])
                except ValueError:
                    print(f"Invalid line: {row}", end="")
            else:
                print(f"Invalid line: {row}", end="")

        prompt = input("Enter the amount to be converted or stop by pressing enter.\n")
        while prompt != "":
            try:
                amount = float(prompt)
                currency = input("Enter the target currency.\n")
                if currency in currency_dictionary:
                    print(f"{amount:0.2f} {file_name[0:3]} = {amount * currency_dictionary[currency]:0.2f} {currency}")
                else:
                    print(f"{currency} is an unknown currency.")
            except ValueError:
                print("Invalid amount!")

            prompt = input("\nEnter the amount to be converted or stop by pressing enter.\n")

    except OSError:
        print(f"Error in reading file {file_name}. Closing program.")


main()
