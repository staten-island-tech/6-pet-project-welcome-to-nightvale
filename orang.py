
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

""" class hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.__money = money
        self.inventory = inventory
    def buy(self, item, cost):
        self.inventory.append(item)
        self.__money -= cost
        print(f"{item} has been added to inventory")
        print(f"{self.name} now has {self.__money} dollars")

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
        print(f"{self.name}'s happiness is now {self.__happiness}") """

""" Angel = BankAccount("Angel", 20000000)
Angel.show_balance()
Angel.deposit(6700)
Angel.show_balance()
Kon = Pet("Kon", 0)
Kon.play()
Kon.show_status() """

""" Angel.buy("goyco", 2) """

""" class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"

class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Student ID: {self.subject}"
    
angel = Student("Angel", "angel@example.com", "0001")
whalen = Teacher("Mr. Whalen", "whalen@example.com", "compsci")

print(angel.display_info())
print(whalen.display_info())
 """