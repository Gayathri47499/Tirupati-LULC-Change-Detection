import numpy as np

# Load stacked images
year1 = np.load("data/year1_stack.npy")
year2 = np.load("data/year2_stack.npy")

# Bands: [Blue, Green, Red, NIR]
y1_red = year1[:, :, 2]
y1_nir = year1[:, :, 3]

y2_red = year2[:, :, 2]
y2_nir = year2[:, :, 3]

# NDVI formula
ndvi1 = (y1_nir - y1_red) / (y1_nir + y1_red + 1e-10)
ndvi2 = (y2_nir - y2_red) / (y2_nir + y2_red + 1e-10)

print("NDVI calculated")

# Save NDVI
np.save("data/ndvi1.npy", ndvi1)
np.save("data/ndvi2.npy", ndvi2)
