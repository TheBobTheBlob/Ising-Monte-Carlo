# Creates an animation of the Ising model simulation using matplotlib
# Requires an ffmpeg executable to save the animation as a video file

import math
import random

import matplotlib.animation as animation
from matplotlib import pyplot as plt

import ising

# EDITABLE CONSTANTS
FFMPEG_PATH = r"" # Path to the ffmpeg executable
SIZE = 100  # Size of the grid
TEMPERATURE = 2.4  # Temperature of the simulation
STARTING_STATE = ising.alternating_state  # Initial state of the grid
FRAMES = 175  # Number of frames in the animation


model = ising.Model(SIZE, STARTING_STATE, TEMPERATURE, ising.kB, ising.J)


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


fig, ax = plt.subplots(dpi=1920 / 16)
mat = ax.matshow(model.grid, cmap="hot", interpolation="nearest")
ani = animation.FuncAnimation(fig, update, frames=FRAMES)

plt.rcParams["animation.ffmpeg_path"] = FFMPEG_PATH
FFwriter = animation.FFMpegWriter()
ani.save("animation.mp4", writer=FFwriter)

plt.show()
