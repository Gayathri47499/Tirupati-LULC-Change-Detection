import numpy as np
import joblib

print("Loading model...")
model = joblib.load("data/lulc_model.pkl")

print("Loading data...")
year1 = np.load("data/year1_stack.npy")[::4, ::4]
year2 = np.load("data/year2_stack.npy")[::4, ::4]
ndvi1 = np.load("data/ndvi1.npy")[::4, ::4]
ndvi2 = np.load("data/ndvi2.npy")[::4, ::4]

print("Reduced image size:", year1.shape)

feat1 = np.dstack((year1, ndvi1))
feat2 = np.dstack((year2, ndvi2))

h, w, f = feat1.shape

print("Predicting...")
lulc1 = model.predict(feat1.reshape(-1, f)).reshape(h, w)
lulc2 = model.predict(feat2.reshape(-1, f)).reshape(h, w)

np.save("data/lulc_year1.npy", lulc1)
np.save("data/lulc_year2.npy", lulc2)

print("LULC maps saved FAST!")
