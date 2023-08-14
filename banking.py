
print('#BANK ACCOUNT DETAILS#')
input('\nfull name:')
input('address:')
input('account number:')

class Bankaccount:
    def __init__(self):
        self.balance=0
        print('welcome to banking system')

    def deposit(self):
        amount_deposited=int(input('\nAmount deposited:'))
        self.balance+=amount_deposited
        print('amount deposited=',amount_deposited)
    def withdraw(self):
        amount_withdraw=int(input('\nAmount to withdraw:'))
        self.balance-=amount_withdraw
        if self.balance>=amount_withdraw:
            print('\nwithdarw successfully')
        else:
            print('insufficient balance')

    def display(self):
        print('\n\nNet Available Balance= ',self.balance)
A=Bankaccount()
A.deposit()
A.withdraw()
A.display()



