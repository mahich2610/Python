width = 3
height = 8
BLACK = "\u001b[40m"
RESET = "\u001b[0m"
cell_height = 4
cell_width = 11
for row in range(height):
    for i in range(cell_height):
        for col in range(width):
            if (row + col) % 2 == 0:
                print(BLACK + " " * cell_width + RESET, end="")
            else:
                print(" " * cell_width, end="")
        print()