import bank_account


def main():
    acc1 = bank_account.BankAccount("FI5511112222333344", "Kari Kemisti")
    acc1.deposit(112.50)
    print(f"The balance of the first account is {acc1.get_balance():0.2f} eur.")
    print(f"The amount withdrawn from the first account was {acc1.withdraw(90.00):0.2f} eur.")
    acc_no2 = input("Enter the id of the second bank account.\n")
    acc_name2 = input("Enter the owner of the second bank account.\n")
    acc2 = bank_account.BankAccount(acc_no2, acc_name2)
    deposit = input("Enter the amount to be deposited into the second account.\n")
    acc2.deposit(float(deposit))
    print(f"The balance of the second account is {acc2.get_balance():0.2f} eur.")
    withdraw = input("Enter the amount to be withdrawn from the second account.\n")
    print(f"The amount withdrawn was {acc2.withdraw(float(withdraw)):0.2f} eur.")
    print(f"The bank accounts:\n{acc1}\n{acc2}")
    transfer = input("Enter the amount to be transferred.\n")
    if acc1.transfer(float(transfer), acc2):
        print("Transfer from the first account into the second account was successful!")
    else:
        print("It was not possible to carry out the bank transfer!")
    print(f"Bank accounts at the end:\n{acc1}\n{acc2}")


main()
