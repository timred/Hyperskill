import random

rules = {
    "rock": {
        "wins_against": "scissors",
        "loses_against": "paper"
    },
    "paper": {
        "wins_against": "rock",
        "loses_against": "scissors"
    },
    "scissors": {
        "wins_against": "paper",
        "loses_against": "rock"
    }
}


def get_rating(name):
    ratings = open("rating.txt")
    for player in ratings:
        player_name = player.split()[0]
        player_score = player.split()[1]
        if player_name == name:
            return int(player_score)
    return 0


def pick_win(opponent):
    return rules[opponent]["loses_against"]


def winner(player, computer):
    if player == computer:
        return "draw"
    elif rules[player]["wins_against"] == computer:
        return "player"
    elif rules[player]["loses_against"] == computer:
        return "computer"
    else:
        return "unknown"


def play():
    player_name = input("Enter your name: ")
    player_score = get_rating(player_name)
    print(f"Hello, {player_name}")

    while True:
        player_input = input()
        computer = random.choice(list(rules.keys()))

        if player_input == "!exit":
            break

        if player_input == "!rating":
            print(f"Your rating: {player_score}")
            continue

        if player_input not in ["rock", "paper", "scissors"]:
            print("Invalid input")
            continue

        outcome = winner(player_input, computer)
        if outcome == "draw":
            player_score += 50
            print(f"There is a draw ({player_input})")
        elif outcome == "player":
            player_score += 100
            print(f"Well done. The computer chose {computer} and failed")
        elif outcome == "computer":
            player_score += 0
            print(f"Sorry, but the computer chose {computer}")
        else:
            print(f"Something has gone wrong :(")


play()
print("Bye!")
