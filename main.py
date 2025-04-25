import random
import math
import multiprocessing
from dataclasses import dataclass

import ising
from matplotlib import pyplot as plt
from typing import Generator

@dataclass
class Result:
    temperature: float
    average_energy: float
    

# EDITABLE CONSTANTS

kB = 1  # Boltzmann constant
SIZE = 100  # Size of the grid
J = -1  # Interaction energy


def simulation(model: ising.Model, show_graph: bool = False) -> Result:
    energy_list = [model.normalised_energy]
    print(f"Starting simulation: size={model.size} T={model.temperature} J={model.j} kB={model.kB}")
    for _ in range(1000):
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

    average_energy = sum(energy_list[-100:]) / 100
    result = Result(temperature=model.temperature, average_energy=average_energy)

    if show_graph:
        plt.plot(range(len(energy_list)), [i for i in energy_list], label=f"Simulation at T={model.temperature}")
        plt.xlabel("Iterations")
        plt.ylabel("Energy")
        plt.title("Energy vs Iterations")
        plt.legend()
        plt.grid()
        plt.show()

    return result


def model_vary_temperature(minimum_temperature: int, maximum_temperature: int) -> Generator[tuple[ising.Model, bool], None, None]:
    # Returns a tuple of (model, show_graph) for each temperature in the range
    # If show_graph is True, then a graph will be shown for that temperature
    # Graph will then need to be closed manually for the simulation to continue
    for t in range(minimum_temperature, maximum_temperature + 1):
        yield (ising.Model(SIZE, ising.alternating_state, t, kB, J), False)


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    results = pool.starmap(simulation, model_vary_temperature(1, 100))

    with open("results.txt", "w+") as file:
        file.write("\n".join(f"{result.temperature}, {round(result.average_energy, 6)}" for result in results))
