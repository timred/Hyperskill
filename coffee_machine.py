def get_water(cups):
    return 200 * cups


def get_milk(cups):
    return 50 * cups


def get_beans(cups):
    return 15 * cups


def make_coffee():
    cups_required = int(input("Write how many cups of coffee you will need: "))
    print(f"For {cups_required} cups of coffee you will need:")
    print(f"{get_water(cups_required)} ml of water")
    print(f"{get_milk(cups_required)} ml of milk")
    print(f"{get_beans(cups_required)} g of coffee beans")


make_coffee()
