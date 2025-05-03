from matplotlib import pyplot as plt
import csv


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

    fig, axes = plt.subplots(nrows=2)
    plt.tight_layout()
    axes[0].plot(size, temperature, label="Tem")
    axes[0].set_xlabel("Size")
    axes[0].set_ylabel("Specific Heat")
    axes[0].set_title("Specific Heat vs Size")
    axes[0].legend()
    axes[0].set_yscale('log')
    axes[0].set_xscale('log')

    axes[1].plot(size, susceptibility, label="Susceptibility")
    axes[1].set_xlabel("Size")
    axes[1].set_ylabel("Susceptibility")
    axes[1].set_title("Susceptibility vs Size")
    axes[1].legend()
    axes[1].grid()
    axes[1].set_yscale('log')
    axes[1].set_xscale('log')


    plt.show()
