# Plots exponents using results from temperature_results.txt
# File is created by simulate_exponents.py

import csv

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Load exponent results from file
with open("exponent_results.txt", "r") as file:
    csv_file = csv.reader(file)
    size = []
    temperature = []
    susceptibility = []

    for line in csv_file:
        size.append(float(line[0]))
        temperature.append(float(line[1]))
        susceptibility.append(float(line[2]))


def power_law(x, a, b):
    return a * np.power(x, b)


# Plot temperature vs size


fig, axes = plt.subplots(nrows=2)
plt.tight_layout()
axes[0].scatter(size, temperature, label="Temperature")
axes[0].set_xlabel("Size")
axes[0].set_ylabel("Specific Heat")
axes[0].set_title("Specific Heat vs Size")

axes[0].legend()
axes[0].grid()
axes[0].set_yscale("log")
axes[0].set_xscale("log")

# Convert lists to numpy arrays for curve fitting
size = np.array(size)
temperature = np.array(temperature)

# Find the power law fit for temperature
popt, pcov = curve_fit(power_law, size, temperature)
a, b = popt

x_fit = np.linspace(min(size), max(size), 100)
y_fit = power_law(x_fit, a, b)
axes[0].plot(x_fit, y_fit, label=f"y = {a:.2f}x**{b:.2f}")


# Plot susceptibility vs size


axes[1].scatter(size, susceptibility, label="Susceptibility")
axes[1].set_xlabel("Size")
axes[1].set_ylabel("Susceptibility")
axes[1].set_title("Susceptibility vs Size")

# Find the power law fit for susceptibility
popt, pcov = curve_fit(power_law, size, susceptibility)
a, b = popt

x_fit = np.linspace(min(size), max(size), 100)
y_fit = power_law(x_fit, a, b)
axes[1].plot(x_fit, y_fit, label=f"y = {a:.2f}x**{b:.2f}")

axes[1].legend()
axes[1].grid()
axes[1].set_yscale("log")
axes[1].set_xscale("log")


plt.show()
