from matplotlib import pyplot as plt
import csv
import numpy as np
from scipy.optimize import curve_fit


# Plotting the energy vs iterations
with open("exponents.txt", "r") as tve:
    csv_tve = csv.reader(tve)
    size = []
    temperature = []
    susceptibility = []

    for line in csv_tve:
        size.append(float(line[0]))
        temperature.append(float(line[1]))
        susceptibility.append(float(line[2]))

def power_law(x, a, b):
    return a * np.power(x, b)



fig, axes = plt.subplots(nrows=2)
plt.tight_layout()
axes[0].scatter(size, temperature, label="Temperature")
axes[0].set_xlabel("Size")
axes[0].set_ylabel("Specific Heat")
axes[0].set_title("Specific Heat vs Size")

size = np.array(size)
temperature = np.array(temperature)

popt, pcov = curve_fit(power_law, size, temperature)
a, b = popt 

x_fit = np.linspace(min(size), max(size), 100)
y_fit = power_law(x_fit, a, b)
axes[0].plot(x_fit, y_fit, label=f'y = {a:.2f}x**{b:.2f}')

axes[1].scatter(size, susceptibility, label="Susceptibility")

axes[0].legend()
axes[0].set_yscale('log')
axes[0].set_xscale('log')

axes[1].set_xlabel("Size")
axes[1].set_ylabel("Susceptibility")
axes[1].set_title("Susceptibility vs Size")

popt, pcov = curve_fit(power_law, size, susceptibility)
a, b = popt 

x_fit = np.linspace(min(size), max(size), 100)
y_fit = power_law(x_fit, a, b)
axes[1].plot(x_fit, y_fit, label=f'y = {a:.2f}x**{b:.2f}')

axes[1].legend()
axes[1].grid()
axes[1].set_yscale('log')
axes[1].set_xscale('log')


plt.show()
