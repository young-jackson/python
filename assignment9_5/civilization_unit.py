# Y1 SUMMER 2022
# Basic Course in Programming Y1
# Author: Joel Lahenius
# Template for exercise 9.5 CivilizationUnit

import random

class CivilizationUnit:

    MAX_HP = 100
    DAMAGE_SCALE = 30
    RANDOM_DAMAGE_DIFF = 8

    def __init__(self, unit_name, attack, defense=None, is_ranged=False):
        """Initializes a new CivilizationUnit"""
        self.__name = unit_name
        self.__attack_strength = attack
        if defense is None:
            self.__defense_strength = attack
        else:
            self.__defense_strength = defense
        self.__fortified = False
        self.__ranged = is_ranged
        self.__hp = CivilizationUnit.MAX_HP


    def get_name(self):
        return self.__name

    def is_alive(self):
        return not self.is_eliminated()

    def is_eliminated(self):
        return self.__hp == 0

    def get_effective_defense_strength(self):
        multiplier = self.__hp / CivilizationUnit.MAX_HP * 0.5 + 0.5
        if self.__fortified:
            multiplier *= 1.4
        return multiplier * self.__defense_strength

    def get_effective_attack_strength(self):
        multiplier = self.__hp / CivilizationUnit.MAX_HP * 0.5 + 0.5
        return multiplier * self.__attack_strength

    def attack(self, other_unit):
        damage_dealt = other_unit.defend(self)
        if self.__ranged:
            damage_taken = 0
        else:
            damage_taken = self.defend(other_unit)
        return damage_dealt, damage_taken

    def defend(self, other_unit):
        excepted_damage_taken = int(CivilizationUnit.DAMAGE_SCALE * other_unit.get_effective_attack_strength() /
                                    self.get_effective_defense_strength())
        actual_damage_taken = max(1, random.randint(excepted_damage_taken - CivilizationUnit.RANDOM_DAMAGE_DIFF,
                                                    excepted_damage_taken + CivilizationUnit.RANDOM_DAMAGE_DIFF))
        if actual_damage_taken > self.__hp:
            self.__hp = 0
        else:
            self.__hp -= actual_damage_taken
        return actual_damage_taken

    def fortify(self):
        self.__fortified = True

    def unfortify(self):
        self.__fortified = False

    def heal(self, amount):
        self.__hp = min(CivilizationUnit.MAX_HP, self.__hp + amount)

    def get_hp(self):
        return self.__hp

    def is_fortified(self):
        return self.__fortified

    def __str__(self):
        if self.is_eliminated():
            add = ", ELIMINATED"
        elif self.__fortified:
            add = ", FORTIFIED"
        else:
            add = ""
        if self.__ranged:
            role = "ranged"
        else:
            role = "melee"
        return_string = f"{self.get_name()} - {self.__attack_strength}/{self.__defense_strength} " \
                        f"({role}) - HP: {self.__hp}{add}"
        return return_string

