import numpy as np
import pandas as pd

lulc1 = np.load("data/lulc_year1.npy").flatten()
lulc2 = np.load("data/lulc_year2.npy").flatten()

df = pd.DataFrame({"From": lulc1, "To": lulc2})

matrix = pd.crosstab(df["From"], df["To"])

print("Transition Matrix:")
print(matrix)

matrix.to_csv("data/transition_matrix.csv")
print("Transition matrix saved!")
