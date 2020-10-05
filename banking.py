import random


class Bank:
    cards = dict()

    def __init__(self):
        self.bank_id_number = '400000'
        self.account_id = self.new_account_id()
        self.checksum = str(luhn(self.bank_id_number + self.account_id, validate=False))
        self.card_number = self.bank_id_number + self.account_id + self.checksum
        self.pin = new_pin()
        self.balance = 0
        self.cards[self.card_number] = self

    def new_account_id(self):
        while True:
            account_id = str(random.randint(0, 999999999))
            account_id = account_id.zfill(9)
            for card_number in self.cards.keys():
                if self.cards[card_number].account_id == account_id:
                    continue
            return account_id


def luhn(number, validate=True):
    card_ints = [int(digit) for digit in number]
    checksum = 0
    if validate:
        checksum = card_ints[-1]
        card_ints = card_ints[:-1]
    card_ints = [digit * 2 if index % 2 == 0 else digit for index, digit in enumerate(card_ints)]
    card_ints = [digit - 9 if digit > 9 else digit for digit in card_ints]
    if not validate:
        return (10 - sum(card_ints) % 10) % 10
    if (10 - sum(card_ints) % 10) % 10 == checksum:
        return True
    else:
        return False


def new_pin():
    pin = str(random.randint(0, 9999))
    pin = pin.zfill(4)
    return pin


def authenticate(card_number, pin_number):
    if card_number in Bank.cards and Bank.cards[card_number].pin == pin_number:
        return True
    else:
        return False


def menu(i):
    if i == 0:
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
    if i == 1:
        print("1. Balance")
        print("2. Log out")
        print("0. Exit")


def main():
    while True:
        menu(0)
        choice = int(input())

        if choice == 1:
            card = Bank()
            print("Your card number:")
            print(card.card_number)
            print("Your card PIN:")
            print(card.pin)
        elif choice == 2:
            card_number = input("Enter your card number:\n")
            pin_number = input("Enter you PIN:\n")
            if authenticate(card_number, pin_number):
                print("You have successfully logged in!")
                card = Bank.cards[card_number]
                while True:
                    menu(1)
                    choice = int(input())
                    if choice == 1:
                        print(f"Balance: {card.balance}")
                    elif choice == 2:
                        print("You have successfully logged out!")
                        break
                    elif choice == 0:
                        break
                if choice == 0:
                    break
            else:
                print("Wrong card number or PIN!")
        elif choice == 0:
            break
    print("Bye!")


main()
