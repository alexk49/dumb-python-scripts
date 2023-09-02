"""Methods with _ before them should only be accessible by the class itself.
This demonstrates the potential issues with not respecting private methods.
The ledger txt files that get created are not creating a full record as we would like."""

class BankAccount:
    def __init__(self, accountHolder):
        # BankAccount methods can access self._balance, but code outside
        # this class should not:
        self._balance = 0
        self._name = accountHolder
        with open(self._name + 'Ledger.txt', 'w') as ledgerFile:
            ledgerFile.write('Balance is 0\n')

    def deposit(self, amount):
        if amount <= 0:
            return # Don't allow negative deposits.
        self._balance += amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Deposit ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return # Not enough in account, or withdraw is negative
        self._balance -= amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Withdraw ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')


acct = BankAccount('Alice') # We create an account for Alice
acct.deposit(120) # _balance can be affected through deposit()
acct.withdraw(40) # _balance can be affect through withdraw

# changing _name or +balance outside of BankAccount is impolite but allowed
acct._balance = 1000000

acct.withdraw(1000)

acct._name = 'Bob' # now we're modifying Bob's account ledger
acct.withdraw(1000)
