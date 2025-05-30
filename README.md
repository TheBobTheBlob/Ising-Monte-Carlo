# Ising Model Monte Carlo Simulation

This project simulates a 2-dimensional Ising spin model using a Monte Carlo method (Metropolis algorithm) in Python. The Ising model is a mathematical model of ferromagnetism in statistical mechanics. The goal of this project is to find the critical temperature of the magnetic material through statistical methods. Created as a college honours project at Missouri S&T.

<p align="center">
  <img src=".github/animation.gif" width="750" alt="Animation of simulation"/>
</p>

> [!NOTE]
> The animation above is of a 100x100 Ising model starting from an alternating state going to equilibrium at a temperature of 2.4

## Explanation

To find the critical temperature, we use the change of different state variables (energy, specific heat, magnetisation, and susceptibility) as temperature changes. Specifically, there should be a point where the rate of change of the variable maximises or the value of the variable itself peaks. To do so, we:

1. Run a simulation at a temperature until the energy of the Ising model equilibrates.
2. Run it for longer.
3. Take the average of the last 100 equilibrium states for all the state variables.
4. Save the results to an external file for later plotting.
5. Plot the results and find the critical temperature.

- `ising.py` contains the implementation of the Ising model itself, a function that runs a simulation, and several helper functions for simulations
- `simulate_temperature.py` runs simulations across a range of temperatures
- `plot_temperature.py` plots the energy, specific heat, magnetization, and susceptibility versus energy

> [!TIP]
> `simulate_temperature.py` and `plot_temperature.py` save/use data from a file called `temperature_results.txt`

Beyond this, we also ran this process across a range of lattice sizes to find the values of some of the exponents of the Ising model using the power-law relation between the exponentials and the size of the lattice.

- `simulate_exponent.py` runs simulations across a range of temperatures at different lattice sizes
- `plot_exponent.py` plots data as well a line of best fit of specific heat and susceptibility versus size
- `plot_single.py` plots the energy vs iterations of a single simulation at a given temperature
- `animate.py` creates an animation of the Ising model lattice as it goes its iterations and saves it as an mp4

> [!TIP]
> `simulate_exponent.py` and `plot_exponent.py` save/use data from a file called `exponent_results.txt`

## Running the algorithm

Ising model specific settings such as the value for `kB`, `J`, and number of iterations can be changed at the top of `ising.py`. Each of the `simulate_*` files also contain settings that can be changed. The results from the simulations can then be plotted using their respective plotting file. As `plot_single.py` runs its own simulation, it also has a few settings near the top.

```shell
python simulate_temperature.py
```

```shell
python plot_temperature.py
```

## Setup

> [!IMPORTANT]  
> The path to an `ffmpeg` executable needs to be entered into `animate.py` for it to successfully create an mp4 file

Install dependencies using pip.

```shell
python -m pip install -r requirements.txt
```
