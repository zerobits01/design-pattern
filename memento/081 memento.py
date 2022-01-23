class Memento:
    def __init__(self, balance):
        self.balance = balance

# look at the initiator
# we can define what should be saved in memento
# most important things

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento):
        self.balance = memento.balance

    def __str__(self):
        return f'Balance = {self.balance}'


# memento acts like snapshots of the system
# after each change we can create a memento and
# later we can restore this
# its just like a transaction save-point


if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    # restore to m1
    ba.restore(m1)
    print(ba)

    # restore to m2
    ba.restore(m2)
    print(ba)