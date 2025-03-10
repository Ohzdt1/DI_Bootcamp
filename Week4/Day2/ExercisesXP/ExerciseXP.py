#🌟 Exercise 1: Matrix Operations

import numpy as np

# Create a 3x3 matrix
matrix = np.array([[2, 4, 3],
                   [1, 5, 7],
                   [6, 8, 9]])

# Calculate the determinant
determinant = np.linalg.det(matrix)

# Check if the determinant is nonzero before computing the inverse
if determinant != 0:
    inverse_matrix = np.linalg.inv(matrix)
else:
    inverse_matrix = "Matrix is singular and has no inverse."

# Display results
print("Matrix:\n", matrix)
print("Determinant:", determinant)
print("Inverse:\n", inverse_matrix)


#🌟 Exercise 2: Statistical Analysis

# 50 random numbers array
random_numbers = np.random.rand(50) * 100  

# Calculate statistical measures
mean_value = np.mean(random_numbers)
median_value = np.median(random_numbers)
std_deviation = np.std(random_numbers)

# Display results
print("Random Numbers:\n", random_numbers)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)


#🌟 Exercise 3: Date Manipulation

# Create an array of dates for January 2023
dates = np.arange('2023-01-01', '2023-02-01', dtype='datetime64[D]')

# Convert to desired format (YYYY/MM/DD)
formatted_dates = np.datetime_as_string(dates, unit='D')

# Display results
print("Dates in YYYY/MM/DD format:\n", formatted_dates)


#🌟 Exercise 4: Data Manipulation with NumPy and Pandas

import pandas as pd

# Create a DataFrame with random numbers
df = pd.DataFrame(np.random.randint(1, 100, (5, 3)), columns=['A', 'B', 'C'])

# Conditional selection (values greater than 50)
filtered_df = df[df > 50]

# Aggregation functions
sum_values = df.sum()
average_values = df.mean()

# Display results
print("Original DataFrame:\n", df)
print("\nFiltered DataFrame (values > 50):\n", filtered_df)
print("\nColumn-wise Sum:\n", sum_values)
print("\nColumn-wise Average:\n", average_values)


#🌟 Exercise 5 : Image Representation

#Images are stored as arrays of pixel values. The way they are represented depends on the type of image

import matplotlib.pyplot as plt

# Create a 5x5 grayscale image (random values from 0 to 255)
image = np.random.randint(0, 256, (5, 5))

# Display the image using Matplotlib
plt.imshow(image, cmap='gray')
plt.colorbar()
plt.title("5x5 Grayscale Image")
plt.show()

# Print pixel values
print("Grayscale Image Pixel Values:\n", image)


#🌟 Exercise 6: Basic Hypothesis Testing

#Hypothesis: "The training program improves employee productivity."
#Test: Comparing productivity before and after using statistical functions.

# Productivity scores before and after training
productivity_before = np.random.normal(50, 10, 30)
productivity_after = productivity_before + np.random.normal(5, 3, 30)

# Compute mean difference
mean_before = np.mean(productivity_before)
mean_after = np.mean(productivity_after)
improvement = mean_after - mean_before

# Display results
print("Mean Productivity Before Training:", mean_before)
print("Mean Productivity After Training:", mean_after)
print("Improvement:", improvement)


#🌟 Exercise 7: Complex Array Comparison

# Create two random arrays
array1 = np.random.randint(1, 100, 10)
array2 = np.random.randint(1, 100, 10)

# Element-wise comparison
comparison = array1 > array2

# Display results
print("Array 1:", array1)
print("Array 2:", array2)
print("Comparison (Array1 > Array2):", comparison)


#🌟 Exercise 8 : Time Series Data Manipulation

# Generate a time series for 2023
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Slicing
Q1 = dates[:90]   
Q2 = dates[90:181]
Q3 = dates[181:273] 
Q4 = dates[273:]

# Display results
print("January to March:\n", Q1)
print("April to June:\n", Q2)
print("July to September:\n", Q3)
print("October to December:\n", Q4)


#🌟 Exercise 9: Data Conversion

# Create a NumPy array
array = np.random.randint(1, 100, (5, 3))

# Convert to Pandas DataFrame
df = pd.DataFrame(array, columns=['A', 'B', 'C'])

# Convert back to NumPy array
array_back = df.to_numpy()

# Display results
print("NumPy Array:\n", array)
print("\nConverted to DataFrame:\n", df)
print("\nBack to NumPy Array:\n", array_back)

# 🌟 Exercise 10 : Basic Visualization

# Generate data
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Plot
plt.plot(x, y, label="Sine Wave", linestyle="--", color='b')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Graph Example")
plt.legend()
plt.show()



