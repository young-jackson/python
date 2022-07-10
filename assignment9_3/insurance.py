class Insurance:
    DEFAULT_DEDUCTIBLE = 150.0
    DEFAULT_CAP = 15000.0
    MAX_BONUS = 70.0
    BONUS_DECREASE = 10.0

    def __init__(self, owner_name, original_premium, given_deductible, cap):
        self.__name = owner_name
        if original_premium < 0:
            self.__premium = 0.0
        else:
            self.__premium = original_premium
        if given_deductible < 0:
            self.__deductible = self.DEFAULT_DEDUCTIBLE
        else:
            self.__deductible = given_deductible
        if cap <= 0:
            self.__total_compensation_cap = self.DEFAULT_CAP
        else:
            self.__total_compensation_cap = cap
        self.__bonus = 0.0
        self.__total_compensations = 0.0
        self.__valid = True

    def get_name(self):
        return self.__name

    def get_bonus(self):
        return self.__bonus

    def get_premium(self):
        return self.__premium

    def get_deductible(self):
        return self.__deductible

    def get_total_compensations(self):
        return self.__total_compensations

    def get_total_compensation_cap(self):
        return self.__total_compensation_cap

    def is_valid(self):
        return self.__valid

    def set_premium(self, new_premium):
        if new_premium >= 0:
            self.__premium = new_premium

    def set_deductible(self, new_deductible):
        if new_deductible >= 0:
            self.__deductible = new_deductible

    def increase_bonus(self, increase):
        if increase >= 0:
            if self.__bonus + increase <= self.MAX_BONUS:
                self.__bonus += increase
            else:
                self.__bonus = self.MAX_BONUS

    def decrease_bonus(self, decrease):
        if decrease >= 0:
            if self.__bonus - decrease >= 0:
                self.__bonus -= decrease
            else:
                self.__bonus = 0.0

    def set_invalid(self):
        self.__valid = False

    def set_valid(self):
        self.__valid = True

    def calculate_real_premium(self):
        return self.__premium * (100 - self.__bonus) / 100.0

    def calculate_compensation(self, damage):
        real_damage = damage - self.__deductible
        if real_damage > 0 and self.is_valid() and self.__total_compensations < self.__total_compensation_cap:
            self.decrease_bonus(10)
            if real_damage + self.__total_compensations <= self.__total_compensation_cap:
                self.__total_compensations += real_damage
                return real_damage
            else:
                decreased_damage = self.__total_compensation_cap - self.__total_compensations
                self.__total_compensations = self.__total_compensation_cap
                return decreased_damage
        else:
            return 0.0

    def __str__(self):
        if self.is_valid():
            insurance = "Insurance policy is valid."
        else:
            insurance = "Insurance policy is not valid."
        l1 = f"Owner: {self.get_name()}, premium {self.get_premium():0.1f} eur / year, bonus {self.get_bonus()} %."
        l2 = f"\nDeductible {self.get_deductible():0.1f} eur, total compensation cap {self.get_total_compensation_cap():0.1f} eur."
        l3 = f"\nTotal compensations currently {self.get_total_compensations()} eur."
        l4 = "\n" + insurance
        return l1 + l2 + l3 + l4

