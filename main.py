import random
from decimal import Decimal
import math

import matplotlib.pyplot as plt
import ising

# EDITABLE CONSTANTS

kB = Decimal(1)  # Boltzmann constant
T = Decimal(2)  # Temperature
SIZE = 100  # Size of the grid
J = Decimal(-1)  # Interaction energy


def simulation(model: ising.Model) -> list[Decimal]:
    energy_list = [model.normalised_energy]
    for _ in range(1000):
        for i, row in enumerate(model.grid):
            for j, _ in enumerate(row):
                delta = model.calculate_delta(i, j)

                if delta <= Decimal(0):
                    model.flip_spin(i, j)
                else:
                    probability = Decimal(math.e) ** (-model.beta * delta)
                    random_value = random.random()

                    if random_value < probability:
                        model.flip_spin(i, j)

        energy_list.append(model.normalised_energy)

    return energy_list


grid = ising.Model(SIZE, ising.alternating_state, T, kB, J)

print(f"\nInitial Energy of the chosen grid: {grid.normalised_energy}")
energy_list = simulation(grid)
print(f"\nEnergy of the final grid: {grid.normalised_energy}")


x = list(range(len(energy_list)))
floated_energy = [float(i) for i in energy_list]

# Plotting the energy vs iterations
plt.plot(x, floated_energy, label="Energy")
plt.xlabel("Iterations")
plt.ylabel("Energy")
plt.title("Energy vs Iterations")
plt.legend()
plt.grid()
plt.show()
