import random
import sqlite3


def create_database():
    conn = sqlite3.connect("card.s3db")
    cur = conn.cursor()
    try:
        cur.execute("drop table card")
        conn.commit()
    except sqlite3.OperationalError:
        pass
    cur.execute("create table if not exists card (id integer, number text, pin text, balance integer default 0)")
    conn.commit()
    conn.close()


class Bank:
    cards = dict()

    def __init__(self):
        self.bank_id_number = '400000'
        self.account_id = new_account_id()
        self.checksum = str(luhn(self.bank_id_number + self.account_id, validate=False))
        self.card_number = self.bank_id_number + self.account_id + self.checksum
        self.pin = new_pin()
        self.balance = 0
        set_card(self)


def new_account_id():
    while True:
        account_id = str(random.randint(0, 999999999))
        account_id = account_id.zfill(9)
        if get_card(account_id):
            continue
        return account_id


def set_card(card):
    query = f"insert into card (id, number, pin, balance) " \
            f"values ({int(card.account_id)}, '{card.card_number}', '{card.pin}', {card.balance})"
    conn = sqlite3.connect("card.s3db")
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def get_card(search):
    query = f"select number, pin, balance from card where number = {search} or id = {search}"
    conn = sqlite3.connect("card.s3db")
    c = conn.cursor()
    c.execute(query)
    card = c.fetchone()
    conn.close()
    return card


def set_balance(card, amount):
    query = f"update card set balance = {amount} where number = '{card}'"
    conn = sqlite3.connect("card.s3db")
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def get_balance(card):
    query = f"select balance from card where number = '{card}'"
    conn = sqlite3.connect("card.s3db")
    c = conn.cursor()
    c.execute(query)
    card = c.fetchone()
    conn.close()
    return card[0]


def valid_card(search):
    query = f"select number from card where number = {search} or id = {search}"
    conn = sqlite3.connect("card.s3db")
    c = conn.cursor()
    c.execute(query)
    card = c.fetchone()
    conn.close()
    return card


def close_account(card_number):
    query = f"delete from card where number = {card_number}"
    conn = sqlite3.connect("card.s3db")
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


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
    card = get_card(card_number)
    if card and card_number == card[0] and pin_number == card[1]:
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
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close Account")
        print("5. Log out")
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
                while True:
                    menu(1)
                    choice = int(input())
                    card = get_card(card_number)
                    if choice == 1:
                        card = get_card(card_number)
                        print(f"Balance: {card[2]}")
                    elif choice == 2:
                        income = int(input("Enter income: "))
                        new_balance = card[2] + income
                        set_balance(card_number, new_balance)
                        print("Income was added!")
                    elif choice == 3:
                        print("Transfer")
                        dest_card = input("Enter card number: ")
                        if not luhn(dest_card, validate=True):
                            print("Probably you made a mistake in the card number. Please try again!")
                            continue
                        if valid_card(dest_card):
                            amount = int(input("Enter how much money you want to transfer: "))
                            if amount > card[2]:
                                print("Not enough money!")
                            else:
                                dest_balance = get_balance(dest_card)
                                dest_balance += amount
                                new_balance = card[2] - amount
                                set_balance(card_number, new_balance)
                                set_balance(dest_card, dest_balance)
                                print("Success!")
                        else:
                            print("Such a card does not exist.")
                    elif choice == 4:
                        close_account(card_number)
                        print("The account has been closed!")
                        break
                    elif choice == 5:
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


create_database()
main()
