# Simulate the exponents of the Ising model by varying the temperature and size of the grid
# Results are written to a file named exponent_results.txt

import multiprocessing
from dataclasses import dataclass

import ising

# EDITABLE CONSTANTS
STARTING_TEMP = 1  # Temperature simulation starts at
ENDING_TEMP = 5  # Temperature simulation ends at
FACTOR = 20  # Factor by which the integer temperature is divided by to get float temperatures

STARTING_SIZE = 4  # Minimum size of the grid (in multiples of 5)
ENDING_SIZE = 20  # Maximum size of the grid (in multiples of 5)


@dataclass
class Max:
    specific_heat: float
    susceptibility: float
    size: int


if __name__ == "__main__":
    maxes = []

    # Iterate through sizes from STARTING_SIZE to ENDING_SIZE
    for i in range(STARTING_SIZE, ENDING_SIZE + 1):
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        results = pool.starmap(ising.simulation, ising.vary_temperature(STARTING_TEMP, ENDING_TEMP, FACTOR, i * 5, ising.down_state))

        maxes.append(
            Max(
                specific_heat=max(results, key=lambda x: x.specific_heat).specific_heat,
                susceptibility=max(results, key=lambda x: x.susceptibility).susceptibility,
                size=i * 5,
            )
        )

    maxes.sort(key=lambda x: x.size)

    with open("exponent_results.txt", "w+") as file:
        file.write(
            "\n".join(
                f"{result.size}, {round(result.specific_heat, 6)}, {round(result.susceptibility, 6)}"
                for result in maxes
            )
        )
