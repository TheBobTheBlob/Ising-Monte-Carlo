import math
import random
from dataclasses import dataclass
from typing import Callable, Generator

from matplotlib import pyplot as plt

# EDITABLE CONSTANTS
kB = 1  # Boltzmann constant
J = -1  # Interaction energy
ITERATIONS = 600  # Number of iterations for the simulation


# STATE GENERATORS
# These functions generate the initial state of the grid based on the given parameters (i, j)


def down_state(i: int, j: int) -> int:
    # Always returns a state of -1
    return -1


def up_state(i: int, j: int) -> int:
    # Always returns a state of 1
    return 1


def alternating_state(i: int, j: int) -> int:
    # Alternates between -1 and 1
    if (i + j) % 2 == 0:
        return 1
    else:
        return -1


def random_state(i: int, j: int) -> int:
    # Randomly returns either an up or down state
    return random.choice([-1, 1])


# ISING MODEL CLASS


class Model:
    """
    Spins are represented by -1 and 1
    -1 = down
    1 = up
    """

    def __init__(self, size: int, create_func: Callable, temperature: float, kB: int, j: int) -> None:
        self.size = size
        self.create_func = create_func
        self.temperature = temperature
        self.kB = kB
        self.j = j

        self.beta = 1 / (self.kB * self.temperature)
        self.sites = self.size**2

        # Initialize the grid with the given state generator function
        self._initialise_grid()
        self.energy = self.calculate_energy()

    def _initialise_grid(self) -> None:
        self.grid: list[list[int]] = []

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.create_func(i, j))
            self.grid.append(row)

    def _opposite_spin(self, i: int, j: int) -> int:
        # Returns the opposite spin of the given cell
        if self.grid[i][j] == -1:
            return 1
        else:
            return -1

    def print(self) -> None:
        # Prints the grid to the console
        for row in self.grid:
            print(" ".join(f" {str(cell)}" if str(cell) == "1" else str(cell) for cell in row))

    def _calculate_neighbours(self, i: int, j: int) -> int:
        # Calculate the sum of the neighbours times J
        # Neighbours are defined as the sum of the four adjacent cells (up, down, left, right)
        return self.j * (
            self.grid[(i + 1) % self.size][j]
            + self.grid[i][(j + 1) % self.size]
            + self.grid[i - 1][j]
            + self.grid[i][j - 1]
        )

    def calculate_energy(self) -> float:
        # Calculate_energy should be calculating the energy of the grid from scratch
        energy = 0
        for i in range(self.size):
            for j in range(self.size):
                energy += self._calculate_neighbours(i, j) * self.grid[i][j]

        return energy / 2

    def calculate_delta(self, i: int, j: int) -> int:
        # calculate_delta should be calculating the change in energy because of one flip
        neighbours = self._calculate_neighbours(i, j)

        energy_before = neighbours * self.grid[i][j]
        energy_after = neighbours * self._opposite_spin(i, j)

        return energy_after - energy_before

    def flip_spin(self, i: int, j: int) -> None:
        # Flips the spin of the given cell
        self.grid[i][j] = self._opposite_spin(i, j)
        self.energy -= self.calculate_delta(i, j)

    @property
    def normalised_energy(self):
        # Normalises the energy to a per-cell basis
        return self.energy / self.sites

    @property
    def microstates(self) -> int:
        # Returns the number of microstates for the given grid size
        return 2 ** (self.sites)

    @property
    def magnetisation(self) -> int:
        # Returns the magnetisation of the grid
        return sum([sum(row) for row in self.grid])

    @property
    def normalised_magnetisation(self) -> float:
        # Returns the normalised magnetisation of the grid
        return self.magnetisation / self.sites


# SIMULATION AND RESULTS


@dataclass
class Result:
    temperature: float
    average_energy: float
    specific_heat: float
    magnetisation: float
    susceptibility: float


def simulation(model: Model, show_graph: bool = False) -> Result:
    # Runs a simulation of the Ising model for a given temperature and returns the results
    # If show_graph is True, then a graph will be shown for the simulation

    energy_list = [model.normalised_energy]
    magnetisation_list = [model.normalised_magnetisation]
    print(f"Starting simulation: size={model.size} T={model.temperature} J={model.j} kB={model.kB}")

    for _ in range(ITERATIONS):
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

    # average energy is the average of the last 100 energies
    average_energy = sum(energy_list[-100:]) / 100

    # squared average energy is the average of the last 100 energies squared
    squared_average_energy = sum([i**2 for i in energy_list[-100:]]) / 100

    # specific heat is the variance of the energy divided by kB * T^2
    specific_heat = model.sites * (squared_average_energy - average_energy**2) / (kB * model.temperature**2)

    # magnetic susceptibility
    average_magnetisation = sum(magnetisation_list[-100:]) / 100
    squared_average_magnetisation = sum([i**2 for i in magnetisation_list[-100:]]) / 100
    susceptibility = (
        model.sites / (model.temperature * model.kB) * (squared_average_magnetisation - average_magnetisation**2)
    )

    result = Result(
        temperature=model.temperature,
        average_energy=average_energy,
        specific_heat=specific_heat,
        magnetisation=model.normalised_magnetisation,
        susceptibility=susceptibility,
    )

    if show_graph:
        plt.plot(range(len(energy_list)), [i for i in energy_list], label=f"Simulation at T={model.temperature}")
        plt.xlabel("Iterations")
        plt.ylabel("Energy")
        plt.title("Energy vs Iterations")
        plt.legend()
        plt.grid()
        plt.show()

    return result


def vary_temperature(start_temp: int, end_temp: int, factor: int, size: int, starting_state: Callable) -> Generator[tuple[Model, bool], None, None]:
    # Returns a tuple of (model, show_graph) for each temperature in the range
    # If show_graph is True, then a graph will be shown for that temperature
    # Graph will then need to be closed manually for the simulation to continue

    for t in range(start_temp, (end_temp * factor) + 1):
        yield (Model(size, starting_state, t / factor, kB, J), False)
