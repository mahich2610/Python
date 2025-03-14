width = 30
height = 10
BLUE = "\u001b[44m"
WHITE = "\u001b[47m"
RED = "\u001b[41m"
RESET = "\u001b[0m"
for _ in range(height):
    print(BLUE + " " * (width // 3) +
          WHITE + " " * (width // 3) +
          RED + " " * (width // 3) +
          RESET)