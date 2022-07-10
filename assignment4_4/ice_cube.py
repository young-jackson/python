def ice_cube_heating(energy, mass, start_temp, end_temp):
    if start_temp < 0:
        c = 2.09
    else:
        c = 4.1819
    final_energy = energy - mass * abs(end_temp - start_temp) * c
    real_end_temp = start_temp + energy / mass / c

    if final_energy < 0:
        return 0.0, real_end_temp
    else:
        return final_energy, end_temp


def ice_cube_melting(energy, mass):
    final_energy = energy - mass * 333
    if final_energy < 0:
        return 0.0, False
    else:
        return final_energy, True


def ice_cube_vaporization(energy, mass):
    final_energy = energy - mass * 2260
    if final_energy < 0:
        return 0.0, False
    else:
        return final_energy, True


def print_heating_result(energy_total, mass, temp_init, temp_end, melted, vaporized):
    print("With {:.2f} kJ, an ice cube weighing {:.2f} kg heats from {:.2f} °C to {:.2f} °C."
          .format(energy_total, mass, temp_init, temp_end))
    if not melted and not vaporized:
        print("The ice cube stays solid.")
    elif melted and not vaporized:
        print("The ice cube has melted into fluid water.")
    else:
        print("The ice cube has vaporized and is now water vapor.")


def main():
    print("Welcome to the ice cube simulator! I will tell you stats about heating your ice cube.")
    mass = float(input("What is the mass of the ice cube (in kg)?\n"))
    while mass <= 0.0:
        print("Mass cannot be zero or negative!")
        mass = float(input("What is the mass of the ice cube?\n"))
    temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    while temp_init < -273.15 or temp_init > 0.0:
        print("The ice cube's temperature can't be under the absolute zero or above 0 degrees!")
        temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))
    while energy_total < 0.0:
        print("Energy cannot be negative!")
        energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))

    melted = False
    vaporized = False
    energy_remaining, end_temp = ice_cube_heating(energy_total, mass, temp_init, 0.0)
    if energy_remaining != 0.0:
        energy_remaining, melted = ice_cube_melting(energy_remaining, mass)
        if energy_remaining != 0.0:
            energy_remaining, end_temp = ice_cube_heating(energy_remaining, mass, 0.0, 100.0)
            if energy_remaining != 0.0:
                energy_remaining, vaporized = ice_cube_vaporization(energy_remaining, mass)

    print_heating_result(energy_total, mass, temp_init, end_temp, melted, vaporized)


main()
