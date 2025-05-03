import multiprocessing
from dataclasses import dataclass

import ising
from typing import Generator
from main import  kB, J,  simulation

@dataclass
class Max:
    temperature: float
    susceptibility: float
    size: int

def model_vary_temperature(
    minimum_temperature: int, maximum_temperature: int, size: int
) -> Generator[tuple[ising.Model, bool], None, None]:
    # Returns a tuple of (model, show_graph) for each temperature in the range
    # If show_graph is True, then a graph will be shown for that temperature
    # Graph will then need to be closed manually for the simulation to continue
    for t in range(minimum_temperature, (maximum_temperature * 10) + 1):
        yield (ising.Model(size, ising.down_state, t / 10, kB, J), False)


if __name__ == "__main__":
    maxes = []

    for i in range(4, 21):
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        results = pool.starmap(simulation, model_vary_temperature(1, 20, i*5))

        maxes.append(Max(temperature=max(results, key=lambda x: x.specific_heat).specific_heat, susceptibility=max(results, key=lambda x: x.susceptibility).susceptibility, size=i*5))
    
    maxes.sort(key=lambda x: x.size)

    with open("exponents.txt", "w+") as file:
        file.write(
            "\n".join(
                f"{result.size}, {round(result.temperature, 6)}, {round(result.susceptibility, 6)}"
                for result in maxes
            )
        )
