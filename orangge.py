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

pet_name = input("What will you name the creature?")