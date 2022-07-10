# Y1 SUMMER 2022
# Basic Course in Programming Y1
# Author: Ville Piiparinen
# Modified by Joel Lahenius (2019), translated by Venla Mikkola
# Example Solution for Exercise 9.4
#
#
# A program that plays Battleship by using the class Battleship.

from battleship import Battleship

MAX_SHIP_LENGTH = 5
MIN_SHIP_LENGTH = 2
NUMBER_OF_SQUARES = 100


def play_turn(battleship_game):
    """
    The function plays a turn of Battleship. The Battleship object
    that represents the game grid of the player in turn is given
    as parameter.
    """
    print("It's {:s}'s turn.".format(battleship_game.get_player()))
    print("Your grid at the moment:")
    print(battleship_game)
    played_turn = False
    while not played_turn:
        try:
            square = int(input("What square do you want to shoot at? Enter the square number between 1-100:\n"))
            outcome = battleship_game.shoot(square)
            if outcome == Battleship.HIT:
                print("You hit!")
                print()
                played_turn = True
            elif outcome == Battleship.MISS:
                print("You missed!")
                print()
                played_turn = True
            elif outcome == Battleship.OUT:
                print("The square cannot be shot at.")
            else:
                print("[Your class returned wrong value.]")
        except ValueError:
            print("The square coordinate must be integer.")
            

class ShipError(Exception):
    """
    Class describes the exception raising from an invalid ship.
    Luokka, joka kuvaa virheellisesta laivasta syntyvaa poikkeusta
    """


def check_and_convert_into_coordinates(ship_string):
    """
    A helper function that checks that the ship occupies right number of consecutive squares
    and is arranged either horizontally or vertically. Function returns a list that contains
    the ship square coordinates as integers. If the ship is invalid or cannot be converted into
    coordinates, the function raises a ShipError.
    """
    try:
        coordinates = [int(x) for x in ship_string.strip().split(" ")]
    except ValueError:
        raise ShipError("The ship coordinates must be integers!")
    ship_length = len(coordinates)
    if not MIN_SHIP_LENGTH <= ship_length <= MAX_SHIP_LENGTH:
        raise ShipError("The ship length must be between 2-5 squares!")
    for coord in coordinates:
        if not 1 <= coord <= NUMBER_OF_SQUARES:
            raise ShipError("Every coordinate must be between 1-100!")
    diff = coordinates[-1] - coordinates[-2]
    if diff not in (1, 10, -1, -10):
        raise ShipError("The ship must be arranged either horizontally or vertically!")
    for i in range(ship_length - 1, 0, -1):
        if coordinates[i] - coordinates[i - 1] != diff:
            raise ShipError("The ship must be arranged either horizontally or vertically!")
        if sorted([coordinates[i] % 10, coordinates[i - 1] % 10]) == [0, 1]:
            raise ShipError("The ship must occupy consecutive squares!")
    return coordinates


def ships_overlap(ship1, ship2):
    """
    The function checks whether ships overlap. If the two lists of ship
    coordinates (given as parameter) contain same integers, function
    returns True. Otherwise, returns False.
    """
    for item in ship1:
        if item in ship2:
            return True
    return False


def ask_ship_coordinates():
    """
    The function asks the ship coordinates and returns them
    as a list of integers.
    """
    coordinates_entered = False
    while not coordinates_entered:
        ships = []
        print("Enter ships (length between 2-5) separated by a comma and the ship square")
        print("coordinates separated by a space. For example: 13 23, 54 64 74 84 94, 25 26 27")
        ship_info = input().split(",")
        try:
            for i in range(len(ship_info)):
                ship = check_and_convert_into_coordinates(ship_info[i])
                if not ships_overlap(ship, ships):
                    ships += ship
                else:
                    raise ShipError("The ships cannot overlap!")
        except ShipError as e:
            print(e)
        else:
            coordinates_entered = True
    return ships

    
def main():
    print("Welcome to play Battleship!")
    print("The square coordinates on the grid are between 1-100 and increase from left to right and top to bottom.")
    player_name1 = input("Enter the name of the first player:\n")
    print("Arrange your ships. The other player should look elsewhere!")
    ships1 = ask_ship_coordinates()
    
    player_name2 = input("Enter the name of the other player:\n")
    print("Arrange your ships. The first player should look elsewhere!")
    ships2 = ask_ship_coordinates()
        
    game1 = Battleship(player_name1, ships2)
    game2 = Battleship(player_name2, ships1)
    
    game_in_turn = game1
    game_over = False
    while not game_over:
        play_turn(game_in_turn)
        game_over = game_in_turn.game_has_ended()
        if game_in_turn == game2:
            game_in_turn = game1
        else:
            game_in_turn = game2
            
    if game_in_turn == game1:
        winner = game2.get_player()
    else:
        winner = game1.get_player()
    print("Game over! {:s} wins!".format(winner))


main()
