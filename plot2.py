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
    axes[0].set_ylabel("Energy")
    axes[0].set_title("Energy vs Size")
    axes[0].legend()

    axes[1].plot(size, susceptibility, label="Sus")
    axes[1].set_xlabel("Size")
    axes[1].set_ylabel("Sus")
    axes[1].set_title("Sus vs Size")
    axes[1].legend()
    axes[1].grid()


    plt.show()
