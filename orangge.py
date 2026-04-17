class pet:
    def __init__(self, name, hunger, happiness):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
    def feed(self):
        print(f"You feed {self.name}, narrowly avoiding getting bit.")
        self.hunger += 5
        print(f"{self.name}'s hunger is now {self.hunger}. It will never be satisfied.")
    def entertain(self):
        print("You do a jaunty little dance, for fear of disapproval from the creature.")
        self.happiness += 5
        print(f"{self.name}'s happiness is now {self.happiness}. You are safe, for now.")
    def display(self):
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")

pet_name = input("What will you name the creature? ")
pett = pet(pet_name, 10, 10)
print(f"Your pet's name is {pet_name}.")
e = 0
interacting = False
while interacting == False:
    action = input("what would you like to do with your pet? \n Your options are: \n1. feed \n2. entertain \n3. display statistics\nSelect a number: ")
    if action == "1":
        pett.feed()
        e += 1
    if action == "2":
        pett.entertain()
        e += 1
    if action == "3":
        pett.display()
        e += 1
    if e == 0:
        print("Action does not exist, please choose again")
    else:
        print(f"Choose another action to perform")