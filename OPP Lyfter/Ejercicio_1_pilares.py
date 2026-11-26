class BankAccount:
    def __init__(self, balance ):
        self.balance = balance

    def deposit_money(self, amount):
        self.balance += amount
        
    def withdraw_money(self, amount):
        self.balance -= amount
        

class SavingsAccount(BankAccount):

    def __init__(self,min_balance, balance ):
        super().__init__(balance)
        self.min_balance = min_balance 

    def withdraw_money(self, amount):

        if amount <= 0:
            raise ValueError("The amount has to be positive") 
        
        if self.balance - amount >= self.min_balance:                                                                                                  

            super().withdraw_money(amount)

        else:
            raise ValueError(f"Fondos insuficientes: el saldo no puede ser menor a ${self.min_balance}")


my_saving_account = SavingsAccount(min_balance=100, balance= 350)

print(f'Initial Balance ${my_saving_account.balance} minimum balance ${my_saving_account.min_balance}')

my_saving_account.withdraw_money(100)
print(f'Balance after withdraw: ${my_saving_account.balance}')

try:
    my_saving_account.withdraw_money(60.0)
except ValueError as error:
    print(f'Error : {error}')

print(f'Final Balance ${my_saving_account.balance}')