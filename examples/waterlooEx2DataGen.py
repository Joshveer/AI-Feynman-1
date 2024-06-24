import numpy as np

# Number of data points
n = 100000

# Generate random values for mass (m), gravity (g), fluid density (ρ), drag coefficient (Cd), and cross-sectional area (A)
m = np.random.uniform(0.1, 10, n)  # Mass between 0.1 and 10 kg
g = np.random.uniform(0.1, 10, n)   # Acceleration due to gravity (constant)
rho = np.random.uniform(1.0, 1.5, n)  # Fluid density between 1.0 and 1.5 kg/m³
Cd = np.random.uniform(0.1, 1.0, n)  # Drag coefficient between 0.1 and 1.0
A = np.random.uniform(0.01, 1, n)  # Cross-sectional area between 0.01 and 1 m²

# Calculate terminal velocity (vt) using the equation vt = sqrt((2mg)/(ρCdA))
# Add a small epsilon to avoid division by zero
epsilon = 1e-10
vt = np.sqrt((2 * m * g) / (rho * Cd * A + epsilon))

# Calculate the dimensionless quantities
pi1 = vt * np.power(rho / (g * np.power(m, 6) + epsilon), 1/6)
pi2 = A * np.power(rho, 2/3) / np.power(m, 2/3)
pi3 = Cd

# Combine all variables into a single dataset
data = np.column_stack((m, g, rho, Cd, A, vt))

# Save the original dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/WaterlooEx2.txt', data)

# Combine dimensionless quantities into a dataset
data_dimensionless = np.column_stack((pi1, pi2, pi3))

# Save the dimensionless dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/buckinghamWaterlooEx2.txt', data_dimensionless)