# Plot the energy vs iterations of a single Ising model simulation

import math
import random

from matplotlib import pyplot as plt

import ising

# EDITABLE CONSTANTS
SIZE = 100  # Size of the grid
TEMPERATURE = 2.4  # Temperature of the simulation
STARTING_STATE = ising.alternating_state  # Initial state of the grid

model = ising.Model(SIZE, STARTING_STATE, TEMPERATURE, ising.kB, ising.J)


energy_list = [model.normalised_energy]
magnetisation_list = [model.normalised_magnetisation]
for _ in range(600):
    for i, row in enumerate(model.grid):
        for j, _ in enumerate(row):
            delta = model.calculate_delta(i, j)

            if delta <= 0:
                model.flip_spin(i, j)
            else:
                probability = math.e ** (-model.beta * delta)
                random_value = random.random()

                if random_value < probability:
                    model.flip_spin(i, j)

    energy_list.append(model.normalised_energy)
    magnetisation_list.append(abs(model.normalised_magnetisation))

# Plot the energy vs iterations
plt.plot(range(len(energy_list)), energy_list, label=f"Simulation at T={model.temperature}")
plt.xlabel("Iterations")
plt.ylabel("Energy")
plt.title("Energy vs Iterations")
plt.legend()
plt.grid()
plt.show()
