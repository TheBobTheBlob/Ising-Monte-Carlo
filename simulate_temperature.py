# Simulates the Ising model at various temperatures and writes the results to a file
# File is named temperature_results.txt

import multiprocessing

import ising

# EDITABLE CONSTANTS
SIZE = 100  # Size of the grid

STARTING_TEMP = 1  # Temperature simulation starts at
ENDING_TEMP = 40  # Temperature simulation ends at
FACTOR = 10  # Factor by which the integer temperature is divided by to get float temperatures


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    results = pool.starmap(ising.simulation, ising.vary_temperature(STARTING_TEMP, ENDING_TEMP, FACTOR, SIZE, ising.down_state))

    with open("temperature_results.txt", "w+") as file:
        file.write(
            "\n".join(
                f"{result.temperature}, {round(result.average_energy, 6)}, {round(result.specific_heat, 6)},  {round(result.magnetisation, 6)}, {round(result.susceptibility, 6)}"
                for result in results
            )
        )
