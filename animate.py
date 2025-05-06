import random
import math

import ising
from matplotlib import pyplot as plt
import matplotlib.animation as animation


# EDITABLE CONSTANTS

kB = 1  # Boltzmann constant
SIZE = 100  # Size of the grid
J = -1  # Interaction energy


model = ising.Model(SIZE, ising.alternating_state, 2.4, kB, J)

print(f"Starting simulation: size={model.size} T={model.temperature} J={model.j} kB={model.kB}")


def update(frame):
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

    mat.set_data(model.grid)
    return [mat]



fig, ax = plt.subplots(figsize=(16, 9), dpi=1920/16)
mat = ax.matshow(model.grid, cmap="hot", interpolation="nearest")
ani = animation.FuncAnimation(fig, update, frames=150)

plt.rcParams['animation.ffmpeg_path'] =r'C:\Users\Punit\AppData\Roaming\Portable Apps\yt-dlp + ffmpeg\ffmpeg.exe'
FFwriter = animation.FFMpegWriter()
ani.save("animation.mp4", writer=FFwriter)

plt.show()

