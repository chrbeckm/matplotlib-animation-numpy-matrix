import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Einlesen der Daten
matrix = np.loadtxt("data.dat")

# Erstelle der leeren Daten Arrays pro Schritt
x_data = np.zeros(16)
y_data = np.zeros(16)

# Anfang des Plots
fig, ax = plt.subplots()
line, = plt.plot([], [], 'o') # Das Komma ist wichtig, da ein Tupel zurückgegeben wird.

# Die Initialisierung ist ein leerer Plot.
def init():
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    return line,

# Plotten der Daten
def anim_func(j):
    # Abspeichern der neuen Daten
    for i in range(16):
        # abgespeichert als x1 y1 x2 y2
        x_data[i] = matrix[j, 2 * i]
        y_data[i] = matrix[j, 2 * i + 1]
    # Plotten
    line.set_data(x_data, y_data)
    return line,

# Das arange() set ist die Numerierung der frames.
arangiert = np.arange(0, matrix[:, 0].size-1)

# Animierfunktion
# fig ≈ plt.figure()
# func = Animationsfunktion
# frames = array an Zahlen, werden an func übergeben
# intervall = Zeitlicher Abstand zwischen den frames
# init_func = Start"bild"
# blit = Controls whether blitting is used to optimize drawing.
    # Note: when using blitting any animated artists will be drawn according to their zorder.
    #   However, they will be drawn on top of any previous artists, regardless of their zorder.
anim = FuncAnimation(fig, func=anim_func, frames=arangiert,
                        interval=20, init_func=init, blit=True)

# Schreiben in '.gif' mit 25 fps
writer = PillowWriter(fps=25)
anim.save("animation.gif", writer=writer)
