def get_water(cups):
    return 200 * cups


def get_milk(cups):
    return 50 * cups


def get_beans(cups):
    return 15 * cups


class CoffeeMachine:
    def __init__(self):
        self.water = int(input("Write how many ml of water the coffee machine has: "))
        self.milk = int(input("Write how many ml of milk the coffee machine has: "))
        self.beans = int(input("Write how many grams of coffee beans the coffee machine has: "))

    def get_stock(self):
        return min(self.water // 200, self.milk // 50, self.beans // 15)

    def make_coffee(self, cups):
        stock = self.get_stock()
        if stock == cups:
            print("Yes, I can make that amount of coffee")
        elif stock > cups:
            print(f"Yes, I can make that amount of coffee (and even {stock - cups} more than that)")
        else:
            print(f"No, I can make only {self.get_stock()} cups of coffee")


my_coffee_machine = CoffeeMachine()

cups_required = int(input("Write how many cups of coffee you will need: "))
my_coffee_machine.make_coffee(cups_required)
