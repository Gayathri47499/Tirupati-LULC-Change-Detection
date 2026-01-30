import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

print("Loading data...")

year1 = np.load("data/year1_stack.npy")
ndvi1 = np.load("data/ndvi1.npy")

features = np.dstack((year1, ndvi1))
h, w, f = features.shape
X = features.reshape(-1, f)

print("Total pixels:", X.shape[0])

# 🔥 TAKE ONLY 50,000 RANDOM PIXELS
sample_size = 50000
indices = np.random.choice(X.shape[0], sample_size, replace=False)
X_sample = X[indices]

# Dummy labels (temporary)
y_sample = np.random.randint(0, 5, sample_size)

print("Training with sample size:", sample_size)

X_train, X_test, y_train, y_test = train_test_split(X_sample, y_sample, test_size=0.2)

model = RandomForestClassifier(n_estimators=50)
model.fit(X_train, y_train)

print("Model trained successfully!")

joblib.dump(model, "data/lulc_model.pkl")
