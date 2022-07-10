# Y1 SUMMER 2022
# A class given in Exercise 9.2
# Author Kerttu Pollari-Malmi
#
# The BankAccount class represents one bank account.

class BankAccount:
    
    # The __init__ method creates a new BankAccount object. The parameters
    # are two strings: the account id and the name of the owner.
    
    def __init__(self, account_no, owner):
        self.__id = account_no
        self.__name = owner
        self.__balance = 0.0
    
    
    # The method returns the account id as a string.
       
    def get_id(self):
        return self.__id
       
    
    # The method returns the name of the owner as a string.
    
    def get_name(self):
        return self.__name
    
    
    # The method returns the balance of the account as a float value.
    
    def get_balance(self):
        return self.__balance
    
    
    # The method makes a deposit into the account. The amount
    # to be deposited (a float value) is given as a parameter.
    
    def deposit(self, amount):
        if amount > 0.0:
            self.__balance += amount
    
    
    # The method withdraws a value given as a parameter (a float value)
    # from the account, if the amount is at most the balance of the
    # account. The method returns the amount which was withdrawn.
                
    def withdraw(self, amount):
        if amount > 0.0 and amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return 0.0
    

    # The method transfers the amount given as a parameter (a float
    # value) from this account to the account given as a parameter,
    # if the amount is positive and at most the balance of this account.
    # The method returns True, if the transfer is successful and otherwise
    # False.
    
    def transfer(self, amount, another_account):
        if self.withdraw(amount) > 0.0:
            another_account.deposit(amount)
            return True
        else:
            return False
        
    
    # The method returns a string containing the id, owner and balance
    # of the accoung.
    
    def __str__(self):
        str1 = "Account {:s}, owner {:s}, balance {:.2f} eur.".format(
                self.__id, self.__name, self.__balance)
        return str1
