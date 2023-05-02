import numpy as np
from scipy.optimize import curve_fit
import csv

# Load data from CSV file
with open('C:\\Users\\User\\OneDrive\\Desktop\\Motor_position', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    #header = next(csvreader)
    for i in range(5):
        next(csvreader)
    row_of_data = next(csvreader)


# Convert data to numpy arrays
x_data = np.array(range(len(row_of_data)))
y_data = np.array(row_of_data, dtype=float)

# Define the sine wave function to fit
def sine_func(x, A, B, C, D):
    return A * np.sin(B * x + C) + D

# Fit the sine wave to the data
initial_guess = [15, 0.1, 0, 120]
fit_params, _ = curve_fit(sine_func, x_data, y_data, p0=initial_guess)

# Print the fit parameters
print(fit_params)
print(fit_params[0],"*sin(",fit_params[1],"*t)+",fit_params[2],"+",fit_params[3],")")

# Plot the data and fitted sine wave
import matplotlib.pyplot as plt

plt.plot(x_data, y_data, label='Data')
plt.plot(x_data, sine_func(x_data, *fit_params), label='Fit')
plt.legend()
plt.show()
