import numpy as np

# Load LULC maps
lulc1 = np.load("data/lulc_year1.npy")
lulc2 = np.load("data/lulc_year2.npy")

print("Detecting change...")

change_map = lulc1 != lulc2  # True where change happened

print("Total changed pixels:", np.sum(change_map))

np.save("data/change_map.npy", change_map)

print("Change map saved!")
