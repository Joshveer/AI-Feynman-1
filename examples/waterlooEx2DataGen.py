import numpy as np

# Number of data points
n = 100000

# Generate random values, avoiding zero
m = np.random.uniform(0.001, 10, n)  # Mass
g = np.random.uniform(0.1, 10, n)  # Gravity
p = np.random.uniform(0.001, 5, n)  # Density
area = np.random.uniform(0.001, 10, n)  # Area
vt = np.random.uniform(0.001, 10, n)  # Terminal velocity

# Calculate Cd, avoiding division by zero
Cd = 2 * m * g / (p * area * (vt**2 + 1e-10))

# Clip Cd to a reasonable range
Cd = np.clip(Cd, 0, 1e5)

# Combine all variables into a single dataset
data = np.column_stack((m, g, p, area, vt, Cd))

# Remove any rows with inf or nan
data = data[~np.isnan(data).any(axis=1) & ~np.isinf(data).any(axis=1)]

# Save the dataset to a text file in a specific directory
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/WaterlooEx2.txt', data)

# Calculate dimensionless parameters
pi1 = vt / ((area ** 0.25) * (g**0.5))
pi2 = m / (p * area**1.5)
pi3 = Cd

data = np.column_stack((pi1, pi2, pi3))

# Remove any rows with inf or nan
data = data[~np.isnan(data).any(axis=1) & ~np.isinf(data).any(axis=1)]

np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/buckinghamWaterlooEx2.txt', data)