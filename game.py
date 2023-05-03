import random

rules = dict()


def set_rules(options):
    for option in options:
        after = [options[i] for i in range(options.index(option) + 1, len(options))]
        before = [options[i] for i in range(0, options.index(option))]
        remains = after + before
        losers = [loser for loser in remains[len(remains) // 2:]]
        rules[option] = losers


def get_rating(name):
    ratings = open("rating.txt")
    for player in ratings:
        player_name = player.split()[0]
        player_score = player.split()[1]
        if player_name == name:
            return int(player_score)
    return 0


def winner(player, computer):
    if player == computer:
        return "draw"
    elif computer in rules[player]:
        return "player"
    elif player in rules[computer]:
        return "computer"
    else:
        return "unknown"


def play():
    player_name = input("Enter your name: ")
    player_score = get_rating(player_name)
    print(f"Hello, {player_name}")

    options = [option for option in input().split(",")]
    if len(options) == 1:
        options = ["rock", "paper", "scissors"]
    set_rules(options)
    print("Okay, let's start")

    while True:
        player_input = input()
        computer = random.choice(list(rules.keys()))

        if player_input == "!exit":
            break

        if player_input == "!rating":
            print(f"Your rating: {player_score}")
            continue

        if player_input not in options:
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
