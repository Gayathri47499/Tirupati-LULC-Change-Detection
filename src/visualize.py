import numpy as np
import matplotlib.pyplot as plt
import os

# Make outputs folder if not exists
os.makedirs("outputs", exist_ok=True)

print("Loading maps...")
lulc1 = np.load("data/lulc_year1.npy")
lulc2 = np.load("data/lulc_year2.npy")
change = np.load("data/change_map.npy")

# 🔥 Downsample to reduce size (every 4th pixel)
lulc1 = lulc1[::4, ::4]
lulc2 = lulc2[::4, ::4]
change = change[::4, ::4]

print("Reduced shape:", lulc1.shape)

# Softer colors
colors = {
    0: [0.8, 0.8, 0.6],   # Barren
    1: [0.2, 0.4, 1],     # Water
    2: [0.4, 1, 0.4],     # Agriculture
    3: [0, 0.6, 0],       # Forest
    4: [1, 0.6, 0.6]      # Built-up
}

def color_map(lulc):
    rgb = np.zeros((lulc.shape[0], lulc.shape[1], 3))
    for cls, col in colors.items():
        rgb[lulc == cls] = col
    return rgb

print("Saving images...")
plt.imsave("outputs/lulc_year1.png", color_map(lulc1))
plt.imsave("outputs/lulc_year2.png", color_map(lulc2))
plt.imsave("outputs/change_map.png", change, cmap='gray')

print("Maps saved successfully!")
