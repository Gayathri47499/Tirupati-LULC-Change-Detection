import numpy as np
import matplotlib.pyplot as plt

lulc1 = np.load("data/lulc_year1.npy")
lulc2 = np.load("data/lulc_year2.npy")
change = np.load("data/change_map.npy")

# Color map for 5 classes
colors = {
    0: [0.6, 0.4, 0.2],   # Barren - brown
    1: [0, 0, 1],         # Water - blue
    2: [0, 1, 0],         # Agriculture - green
    3: [0, 0.5, 0],       # Forest - dark green
    4: [1, 0, 0]          # Built-up - red
}

def color_map(lulc):
    rgb = np.zeros((lulc.shape[0], lulc.shape[1], 3))
    for cls, col in colors.items():
        rgb[lulc == cls] = col
    return rgb

plt.imsave("outputs/lulc_year1.png", color_map(lulc1))
plt.imsave("outputs/lulc_year2.png", color_map(lulc2))
plt.imsave("outputs/change_map.png", change, cmap='gray')

print("Maps saved in outputs folder!")
