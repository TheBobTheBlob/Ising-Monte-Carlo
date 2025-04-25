from matplotlib import pyplot as plt
import csv


# Plotting the energy vs iterations
with open('results.txt', 'r') as tve:
    csv_tve = csv.reader(tve)
    temperature = []
    energy = []
    specific_heat = []
    magnetisation = []

    for line in csv_tve:
        temperature.append(float(line[0]))
        energy.append(float(line[1]))
        specific_heat.append(float(line[2]))
        magnetisation.append(float(line[3]))

    fig, axes = plt.subplots(nrows=3)
    plt.tight_layout()
    axes[0].plot(temperature, energy, label="Energy")
    axes[0].set_xlabel("Temperature")
    axes[0].set_ylabel("Energy")
    axes[0].set_title("Energy vs Temperature")
    axes[0].legend()

    axes[1].plot(temperature, specific_heat, label="Specific Heat")
    axes[1].set_xlabel("Specific Heat")
    axes[1].set_ylabel("Energy")
    axes[1].set_title("Specific Heat vs Temperature")
    axes[1].legend()
    axes[1].grid()

    axes[2].plot(temperature, magnetisation, label="Magnetisation")
    axes[2].set_xlabel("Magnetisation")
    axes[2].set_ylabel("Energy")
    axes[2].set_title("Magnetisation vs Temperature")
    axes[2].legend()
    axes[2].grid()
    
    plt.show()


    # plt.plot(temperature, energy, label="Energy")
    # plt.xlabel("Temperature")
    # plt.ylabel("Energy")
    # plt.title("Energy vs Temperature")
    # plt.legend()
    # plt.grid()
    plt.show()
