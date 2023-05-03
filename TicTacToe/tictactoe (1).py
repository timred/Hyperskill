grid = [["_", "_", "_", "_", "_", "_", "_", "_", "_", ][i:i+3] for i in range(0, 9, 3)]
player = "X"


def is_full(m):
    total_cells = sum([0 if c == "_" else 1 for r in m for c in r])
    return total_cells == 9


def is_three(m, p):
    count = [1 if c == p else 0 for r in m for c in r]
    row_count = [sum(count[i:i+3]) for i in range(0, len(count), 3)]
    col_count = [sum(count[i::3]) for i in range(3)]
    diagonal_count = [sum(count[::4]), sum(count[2:8:2])]
    return 3 in row_count or 3 in col_count or 3 in diagonal_count


def player_count(m, p):
    count = [1 if c == p else 0 for r in m for c in r]
    return sum(count)


def print_grid():
    print("---------")
    for row in grid:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" ")
        else:
            print("|")
    print("---------")


def check_state():
    if (is_three(grid, "X") and is_three(grid, "O")) or not (-2 < player_count(grid, "X") - player_count(grid, "O") < 2):
        print("Impossible")
        return True
    elif is_three(grid, "X"):
        print("X wins")
        return True
    elif is_three(grid, "O"):
        print("O wins")
        return True
    elif is_full(grid) and (not is_three(grid, "X") or not is_three(grid, "O")):
        print("Draw")
        return True
    elif not is_full(grid) and (not is_three(grid, "X") or not is_three(grid, "O")):
        return False


def is_valid(col, row):
    if col > 3 or row > 3 or col < 0 or row < 0:
        print("Coordinates should be from 1 to 3!")
        return False
    cell = grid[abs(row - 3)][col - 1]
    if cell == "X" or cell == "O":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        return True


def move(p):
    try:
        col, row = input("Enter the coordinates: ").split()
        col = int(col)
        row = int(row)
    except ValueError:
        print("You should enter numbers!")
        return False
    if is_valid(col, row):
        grid[abs(row - 3)][col - 1] = p
        print_grid()
        return True


def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def main():
    print_grid()
    while not check_state():
        if move(player):
            switch_player()


main()
