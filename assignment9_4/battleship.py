class Battleship:
    HIT = 1
    MISS = 0
    OUT = -1

    def __init__(self, player_name, opponent_ships):
        self.__name = player_name
        self.__ships = opponent_ships
        self.__grid = ["_"] * 100

    def get_player(self):
        return self.__name

    def shoot(self, position):
        index = position - 1
        if index in range(100) and self.__grid[index] == "_":
            if position in self.__ships:
                self.__grid[index] = "X"
                return Battleship.HIT
            else:
                self.__grid[index] = "O"
                return Battleship.MISS
        else:
            return Battleship.OUT

    def game_has_ended(self):
        ended = True
        for n in self.__ships:
            if self.__grid[n - 1] != "X":
                ended = False
        return ended

    def __str__(self):
        grid = ""
        for i in range(10):
            for k in range(10):
                grid += self.__grid[i * 10 + k] + " "
            grid = grid.rstrip() + "\n"
        return grid.rstrip()
