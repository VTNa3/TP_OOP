class BankAccount:
    bank_name = "ABA Bank"  # Class attribute

    def __init__(self, owner, balance):
        self.owner = owner                  # Public attribute
        self._account_type = "Saving"       # Protected by convention
        self.__balance = balance            # Private attribute

    def deposit(self, amount):              # Instance method
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def get_balance(self):                  # Instance method
        return self.__balance

    @classmethod                            # Class method
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod                           # Static method
    def is_valid_amount(amount):
        return amount > 0

account1 = BankAccount("Dara", 1000)        # Create an account
print("Owner:", account1.owner)             # Access public attribute
print("Bank:", BankAccount.bank_name)       # Access class attribute

print("Balance:", account1.get_balance())   # Access balance through a method

account1.deposit(500)                       # Deposit money
print("New balance:", account1.get_balance())

BankAccount.change_bank_name("National Bank")# Call a class method
print("New bank name:", BankAccount.bank_name)

print("Is amount valid?", BankAccount.is_valid_amount(200))# Call a static method