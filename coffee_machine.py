class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9

    products = {
        "espresso": {"water": 250, "milk": 0, "beans": 16, "cost": 4},
        "latte": {"water": 350, "milk": 75, "beans": 20, "cost": 7},
        "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cost": 6},
    }

    def action(self):
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
            options = {1: "espresso", 2: "latte", 3: "cappuccino"}
            if selection == "back":
                return 1
            selection = int(selection)
            if self.check_stock(options[selection]):
                print("I have enough resources, making you a coffee!")
                self.make_coffee(options[selection])
        elif action == "fill":
            self.fill_stock()
        elif action == "take":
            self.take_money()
        elif action == "remaining":
            self.get_stock()
        elif action == "exit":
            return 0

    def get_stock(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")

    def fill_stock(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def make_coffee(self, product):
        self.water -= self.products[product]["water"]
        self.milk -= self.products[product]["milk"]
        self.beans -= self.products[product]["beans"]
        self.cups -= 1
        self.money += self.products[product]["cost"]

    def check_stock(self, product):
        if self.water < self.products[product]["water"]:
            print("Sorry, not enough water!")
            return False
        if self.milk < self.products[product]["milk"]:
            print("Sorry, not enough milk!")
            return False
        if self.beans < self.products[product]["beans"]:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < 1:
            print("Sorry, not enough cups!")
            return False
        return True


my_coffee_machine = CoffeeMachine()
while True:
    output = my_coffee_machine.action()
    if output == 0:
        break
    if output == 1:
        continue
