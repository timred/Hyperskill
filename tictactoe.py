# write your code here
print("X O X")
print("O X O")
print("X X O")

cells = input("Enter cells: ")
rows = [cells[i:i+3] for i in range(0, len(cells), 3)]

print("---------")
for row in rows:
    print("|", end=" ")
    for cell in row:
        print(cell, end=" ")
    else:
        print("|")
print("---------")
