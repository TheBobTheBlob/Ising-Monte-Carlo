import random
import math

import ising
from matplotlib import pyplot as plt


# EDITABLE CONSTANTS

kB = 1  # Boltzmann constant
SIZE = 100  # Size of the grid
J = -1  # Interaction energy


model = ising.Model(SIZE, ising.alternating_state, 2.4, kB, J)

print(f"Starting simulation: size={model.size} T={model.temperature} J={model.j} kB={model.kB}")


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


plt.plot(range(len(energy_list)), [i for i in energy_list], label=f"Simulation at T={model.temperature}")
plt.xlabel("Iterations")
plt.ylabel("Energy")
plt.title("Energy vs Iterations")
plt.legend()
plt.grid()
plt.show()
