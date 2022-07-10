# Y1 SUMMER 2022
# Basic Course in Programming Y1
# Author: Joel Lahenius
# A testing program for 9.5 CivilizationUnit

from civilization_unit import CivilizationUnit
import random

MAX_ATTACK = 300
MAX_DEFENSE = MAX_ATTACK
MENU =  "Actions:\n" + \
        "  N - Create a new CivilizationUnit\n" + \
        "  A - Attack (against another unit)\n" + \
        "  H - Heal\n" + \
        "  P - Print unit statuses\n" + \
        "  F - Fortify / Unfortify\n" + \
        "Debugging:\n" + \
        "  X - Print the fields of a CivilizationUnit instance (in raw form)\n" + \
        "Other:\n" + \
        "  Q - Quit"
        
def fight_and_print_outcome(attacker, defender):
    if attacker.is_eliminated():
        print("{:s} could not attack as it is dead".format(attacker.get_name()))
    elif defender.is_eliminated():
        print("{:s} could not be attacked against as it is dead".format(defender.get_name()))
    else:
        damage_dealt, damage_taken = attacker.attack(defender)
        print("The {:s} dealt {:d} damage to the {:s} and took {:d} damage itself.".format(attacker.get_name(), damage_dealt, defender.get_name(), damage_taken))
        
def input_int(low_limit, high_limit, msg = "Enter a number:"):
    choice = low_limit - 1
    while not low_limit <= choice <= high_limit:
        try:
            choice = int(input(msg))
        except ValueError:
            print("Enter your choice as an integer in the range {}-{}".format(low_limit, high_limit))
    return choice

class CivilizationUnitTestingProgram:
    
    """
    Note to students: this testing class is NOT an example of a particularly good class in any way. 
    It was designed just to make a simple testing environment for this exercise. It satisfies that need.
    """
    
    def __init__(self):
        self.units = []
    
    def print_units(self):
        num = 1
        for unit in self.units:
            print("{}. {}".format(num, unit))
            num += 1
        
    def ask_user_to_select_unit(self):
        self.print_units()
        return self.units[input_int(1, len(self.units), "Choose unit number: ") - 1]
    
    def add_unit(self):
        print("Creating a new CivilizationUnit.")
        name = input("Name: ")
        att = input_int(1, MAX_ATTACK, "Attack: ")
        ranged = True if input("Ranged (y/n)?: ").upper()[0] == "Y" else False
        if ranged:
            defe = input_int(1, MAX_DEFENSE, "Defense: ")
        else:
            print("For melee units, defense strength equals attack strength.")
            defe = att
        self.units.append(CivilizationUnit(name, att, defe, ranged))
        print("A new unit created.")
        
    def attack(self):
        if not self.units:
            print("No units created yet.")
            return
        print("Which unit to attack with (attacking unit)?")
        attacker = self.ask_user_to_select_unit()
        print("Which unit to attack against (defending unit)?")
        defender = self.ask_user_to_select_unit()
        print()
        fight_and_print_outcome(attacker, defender)
    
    def heal(self):
        if not self.units:
            print("No units created yet.")
            return
        print("Which unit to heal?")
        to_be_healed = self.ask_user_to_select_unit()
        amount = input_int(0, CivilizationUnit.MAX_HP, "How much to heal (0-{}): ".format(CivilizationUnit.MAX_HP))
        to_be_healed.heal(amount)
        print("Healed {} for {}".format(to_be_healed.get_name(), amount))
        
    def print_unit_statuses(self):
        if not self.units:
            print("No units created yet.")
            return
        self.print_units()
    
    def change_unit_fortification(self):
        if not self.units:
            print("No units created yet.")
            return
        unit = self.ask_user_to_select_unit()
        if unit.is_fortified():
            unit.unfortify()
            start = "Unf"
        else:
            unit.fortify()
            start = "F"
        print("{}ortified {}".format(start, unit.get_name()))
              
    def print_unit_fields_raw(self):
        if not self.units:
            print("No units created yet.")
            return
        print("Which unit to inspect?")
        unit = self.ask_user_to_select_unit()
        fields_dict = unit.__dict__
        for field in sorted(fields_dict):
            print("{:50}: {}".format(field, fields_dict[field]))
    
def main():
    print("This is a testing program to test and debug your class.")
    seed = int(input("Enter a seed for the random generator:\n"))
    random.seed(seed)
    tester = CivilizationUnitTestingProgram()
    actions = {"A": tester.attack,
               "P": tester.print_unit_statuses,
               "H": tester.heal,
               "F": tester.change_unit_fortification,
               "X": tester.print_unit_fields_raw,
               "N": tester.add_unit}
    cont = True
    while cont:
        print()
        print(MENU)
        cmd = input().strip().upper()
        if cmd == "Q":
            print("Quitting...")
            cont = False
        else:
            try:
                actions[cmd]()
            except KeyError:
                print("Invalid action.")
                
if __name__ == "__main__":
    main()
