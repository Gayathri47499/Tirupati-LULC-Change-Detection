import rasterio
import numpy as np


y1_b2 = "data/year1/T44PLA_20180822T050649_B02_10m.jp2"
y1_b3 = "data/year1/T44PLA_20180822T050649_B03_10m.jp2"
y1_b4 = "data/year1/T44PLA_20180822T050649_B04_10m.jp2"
y1_b8 = "data/year1/T44PLA_20180822T050649_B08_10m.jp2"


y2_b2 = "data/year2/T44PLA_20230227T050749_B02_10m.jp2"
y2_b3 = "data/year2/T44PLA_20230227T050749_B03_10m.jp2"
y2_b4 = "data/year2/T44PLA_20230227T050749_B04_10m.jp2"
y2_b8 = "data/year2/T44PLA_20230227T050749_B08_10m.jp2"

def read_band(path):
    with rasterio.open(path) as src:
        return src.read(1)

print("Reading Year 1 bands...")
y1_blue = read_band(y1_b2)
y1_green = read_band(y1_b3)
y1_red = read_band(y1_b4)
y1_nir = read_band(y1_b8)

print("Stacking Year 1...")
year1_stack = np.dstack((y1_blue, y1_green, y1_red, y1_nir))

print("Reading Year 2 bands...")
y2_blue = read_band(y2_b2)
y2_green = read_band(y2_b3)
y2_red = read_band(y2_b4)
y2_nir = read_band(y2_b8)

print("Stacking Year 2...")
year2_stack = np.dstack((y2_blue, y2_green, y2_red, y2_nir))

print("Year 1 shape:", year1_stack.shape)
print("Year 2 shape:", year2_stack.shape)

# Save stacks for next steps
np.save("data/year1_stack.npy", year1_stack)
np.save("data/year2_stack.npy", year2_stack)

print("Stacks saved successfully!")
