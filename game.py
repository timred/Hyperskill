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
    player = input()
    computer = random.choice(list(rules.keys()))

    outcome = winner(player, computer)
    if outcome == "draw":
        print(f"There is a draw ({player})")
    elif outcome == "player":
        print(f"Well done. The computer chose {computer} and failed")
    elif outcome == "computer":
        print(f"Sorry, but the computer chose {computer}")
    else:
        print(f"Something has gone wrong :(")


play()
