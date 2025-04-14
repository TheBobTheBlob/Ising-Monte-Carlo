import random
from decimal import Decimal
import math
import multiprocessing
from dataclasses import dataclass

import ising


@dataclass
class Result:
    temperature: Decimal
    average_energy: Decimal


# EDITABLE CONSTANTS

kB = Decimal(1)  # Boltzmann constant
SIZE = 20  # Size of the grid
J = Decimal(-1)  # Interaction energy


def simulation(model: ising.Model) -> Result:
    energy_list = [model.normalised_energy]
    print(f"Starting simulation: size={model.size} T={model.temperature} J={model.j} kB={model.kB}")
    for _ in range(300):
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

    average_energy = sum(energy_list[-100:]) / Decimal(100)
    result = Result(temperature=model.temperature, average_energy=average_energy)

    return result


def model_vary_temperature(minimum_temperature, maximum_temperature):
    for t in range(minimum_temperature, maximum_temperature + 1):
        yield ising.Model(SIZE, ising.alternating_state, Decimal(t), kB, J)


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=12)
    results = pool.map(simulation, model_vary_temperature(1, 100))

    with open("results.txt", "w+") as file:
        file.write("\n".join(f"{result.temperature}, {result.average_energy}" for result in results))
