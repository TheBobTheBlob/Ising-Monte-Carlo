from matplotlib import pyplot as plt
import csv


# Plotting the energy vs iterations
with open('results.txt', 'r') as tve:
    csv_tve = csv.reader(tve)
    temperature = []
    energy = []
    for line in csv_tve:
        temperature.append(float(line[0]))
        energy.append(float(line[1]))


    plt.plot(temperature, energy, label="Energy")
    plt.xlabel("Temperature")
    plt.ylabel("Energy")
    plt.title("Energy vs Temperature")
    plt.legend()
    plt.grid()
    plt.show()
