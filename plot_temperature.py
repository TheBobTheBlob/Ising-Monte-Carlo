# Plots different state variables against temperature using results from temperature_results.txt
# File is created by simulate_temperature.py

import csv

from matplotlib import pyplot as plt

# Load temperature results from file
with open("temperature_results.txt", "r") as tve:
    csv_tve = csv.reader(tve)
    temperature = []
    energy = []
    specific_heat = []
    magnetisation = []
    susceptibility = []

    for line in csv_tve:
        temperature.append(float(line[0]))
        energy.append(float(line[1]))
        specific_heat.append(float(line[2]))
        magnetisation.append(float(line[3]))
        susceptibility.append(float(line[4]))


# Plot energy vs temperature
fig, axes = plt.subplots(nrows=4)
plt.tight_layout()
axes[0].plot(temperature, energy, label="Energy")
axes[0].set_xlabel("Temperature")
axes[0].set_ylabel("Energy")
axes[0].set_title("Energy vs Temperature")
axes[0].legend()
axes[0].grid()

# Plot specific heat vs temperature
axes[1].plot(temperature, specific_heat, label="Specific Heat")
axes[1].set_xlabel("Temperature")
axes[1].set_ylabel("Specific Heat")
axes[1].set_title("Specific Heat vs Temperature")
axes[1].legend()
axes[1].grid()

# Plot magnetization vs temperature
axes[2].plot(temperature, magnetisation, label="Magnetization")
axes[2].set_xlabel("Temperature")
axes[2].set_ylabel("Magnetization")
axes[2].set_title("Magnetization vs Temperature")
axes[2].legend()
axes[2].grid()

# Plot susceptibility vs temperature 
axes[3].plot(temperature, susceptibility, label="Susceptibility")
axes[3].set_xlabel("Temperature")
axes[3].set_ylabel("Susceptibility")
axes[3].set_title("Susceptibility vs Temperature")
axes[3].legend()
axes[3].grid()

plt.show()
