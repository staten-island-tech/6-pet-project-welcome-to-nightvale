
""" class Calculator():
    def add(x,y):
        print(x + y)
        return x + y
    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)
    def subtract(numbers):
        return numbers
Calculator.add(5,6) """

class hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.__money = money
        self.inventory = inventory
    def buy(self, item, cost):
        self.inventory.append(item)
        self.
        print(self.inventory)

Angel = hero("Angel", 2000000, ["rat", "roblox"])

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
    def play(self):
        self.__happiness += 5
        print(f"{self.name} is playing fetch!")
    def show_status(self):
        print(f"{self.name}'s happiness is now {self.__happiness}")

Angel = BankAccount("Angel", 20000000)
""" Angel.show_balance()
Angel.deposit(6700)
Angel.show_balance() """
Kon = Pet("Kon", 0)
Kon.play()
Kon.show_status()