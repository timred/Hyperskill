import random


class Bank:
    cards = dict()

    def __init__(self):
        self.bank_id_number = '400000'
        self.account_id = self.new_account_id()
        self.checksum = '7'
        self.card_number = self.bank_id_number + self.account_id + self.checksum
        self.pin = new_pin()
        self.balance = 0
        self.cards[self.card_number] = self

    def new_account_id(self):
        account_id = str(random.randint(0, 999999999))
        account_id.zfill(9)
        for card_number in self.cards.keys():
            if self.cards[card_number].account_id == account_id:
                self.new_account_id()
        return account_id


def new_pin():
    pin = str(random.randint(0, 9999))
    pin.zfill(4)
    return pin


def valid_account(card_number, pin_number):
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
            if valid_account(card_number, pin_number):
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
