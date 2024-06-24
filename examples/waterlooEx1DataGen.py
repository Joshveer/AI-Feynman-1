import numpy as np

# Number of data points
n = 100000

# Generate random values for initial position (s₀), initial velocity (v₀), acceleration (g), and time (t)
s0 = np.random.uniform(0, 10, n)  # Initial position between 0 and 10
v0 = np.random.uniform(-5, 5, n)  # Initial velocity between -5 and 5
a = np.random.uniform(-10, 10, n)    # Acceleration between -5 and 5
t = np.random.uniform(0, 5, n)    # Time between 0 and 5

# Calculate displacement (s) using the equation s = s₀ + v₀t + 0.5at²
s = s0 + v0 * t - 0.5 * a * t**2

# Combine all variables into a single dataset
data = np.column_stack((s0, v0, a, t, s))

# Save the dataset to a text file in a specific directory
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/WaterlooEx1.txt', data)

pi1 = s/s0
pi2 = s0*a/(v0**2)
pi3 = v0*t/s0

data = np.column_stack((pi2, pi3, pi1))

np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/buckinghamWaterlooEx1.txt', data)