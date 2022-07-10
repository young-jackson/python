import random


def draw_random_number(numbers):
    n = random.randint(1, 75)
    while n in numbers:
        n = random.randint(1, 75)
    return n


def cross_out_number(grid, number):
    if number in grid:
        p = grid
        p[p.index(number)] = "X"
        return p
    else:
        return grid


def grid_completed(grid):
    x = True
    for i in grid:
        if i != "X":
            x = False
    return x


def print_grid(grid, grid_size):
    for n in range(grid_size):
        for m in range(grid_size):
            print(f"{grid[n * grid_size + m]:>3}", end="")
        print("")


def main():
    names = ["", ""]
    numbers = []

    print("Welcome to play bingo!")
    size = int(input("Enter the size of one side of the grid. The size must be between 3 and 5:\n"))
    while size not in range(3, 6):
        print("The number must be between 3 and 5.")
        size = int(input("Enter a size:\n"))
    random.seed(int(input("Enter a seed:\n")))

    grids = [[0] * size * size, [0] * size * size]

    for i in range(2):
        names[i] = input(f"Enter the name of the {i + 1}. player:\n")
        print(f"{names[i]}, choose different numbers between 1-75.")
        for k in range(size * size):
            prompt = int(input("Enter a number:\n"))
            while prompt in grids[i] or not (1 <= prompt <= 75):
                if not (1 <= prompt <= 75):
                    prompt = int(input("The number must be between 1 and 75. Choose another number:\n"))
                else:
                    prompt = int(input("The number is already in the grid. Choose a different number:\n"))
            grids[i][k] = prompt
        print("The numbers were added successfully.")
        print(f"{names[i]}'s grid:")
        print_grid(grids[i], size)
        print("")

    print("Game starts.")
    while not (grid_completed(grids[0]) or grid_completed(grids[1])):
        input("Press enter to draw a number.\n")
        drawn_number = draw_random_number(numbers)
        numbers.append(drawn_number)
        print(f"The drawn number is {drawn_number}.")

        for i in range(2):
            if drawn_number in grids[i]:
                print(f"{names[i]} crossed out a number {drawn_number}.")
                grids[i] = cross_out_number(grids[i], drawn_number)
        print("")

        for i in range(2):
            print(f"{names[i]}'s grid")
            print_grid(grids[i], size)
            print("")

    for i in range(2):
        if grid_completed(grids[i]):
            print(f"{names[i]} has crossed out all the numbers.")
            print(f"{names[i]} won!")

    print("Game ended.")


main()
