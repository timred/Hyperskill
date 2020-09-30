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


user = input()
computer = pick_win(user)
print(f"Sorry, but the computer chose {computer}")
