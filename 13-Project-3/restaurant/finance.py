class Finance:
    def __init__(self, balance):
        self.bal = balance
        self.log = []

    def debit(self, amount):
        #deducts amount from the current balance, doing nothing if there is not enough. returns a boolean for whether the transaction occurred

        if self.bal >= amount:
            self.bal -= amount
            self.log.append(-amount)
            return True
        else:
            return False

    def credit(self, amount):
        #adds amount to the current balance

        self.bal += amount
        self.log.append(amount)

    def balance(self):
        #returns the current balance

        return self.bal

    def enough_funds(self, amount):
        #returns a boolean indicating if the balance is equal to or larger than amount

        if self.bal >= amount:
            return True
        else:
            return False

    def transaction_log(self):
        #returns a list of the previous valid transactions, as numbers. Debits will be negative, and credits will be positive
        #The first transaction should be first, and the most recent last

        return self.log