import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import ttest_ind


# Load the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "global_power_plant_database.csv")

df = pd.read_csv(file_path)

# Display basic information about the dataset
df_info = df.info()
df_head = df.head()

print(df_info)
print(df_head)

# Count missing values in each column
missing_values_count = df.isnull().sum()

# Display missing values count
print("Missing Values in Each Column:")
print(missing_values_count[missing_values_count > 0])


# Fill missing values for numerical columns with their median (more robust to outliers)
num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = df[num_cols].apply(lambda x: x.fillna(x.median()))

# Fill missing values for categorical columns with 'Unknown'
cat_cols = df.select_dtypes(include=[object]).columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

# Convert commissioning_year to integer since it's now filled
df["commissioning_year"] = df["commissioning_year"].astype(int)

# Verify if missing values are handled
missing_values = df.isnull().sum()

# Display updated summary statistics
summary_statistics = df.describe()

print(f"\nMissing Values After\n", missing_values)
print(summary_statistics)


# Remove negative values from generation data
generation_cols = [col for col in df.columns if "generation_gwh" in col]
for col in generation_cols:
    df[col] = df[col].apply(lambda x: max(x, 0))

# Distribution of power plants by country
top_countries = df["country_long"].value_counts().head(10)

# Distribution of power plants by fuel type 
fuel_distribution = df["primary_fuel"].value_counts().head(10)

# Visualizing power plant distribution by country
plt.figure(figsize=(20, 10))
sns.barplot(x=top_countries.index, y=top_countries.values, 
            palette=sns.color_palette("viridis_r", n_colors=len(top_countries)))
plt.xticks(rotation=45)
plt.title("Top 10 Countries with Most Power Plants")
plt.xlabel("Country")
plt.ylabel("Number of Power Plants")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Visualizing fuel type distribution (limited to top 10 for clarity)
plt.figure(figsize=(10, 5))
sns.barplot(x=fuel_distribution.index, y=fuel_distribution.values, 
            palette=sns.color_palette("Spectral", n_colors=len(fuel_distribution)))
plt.xticks(rotation=45)
plt.title("Top 10 Power Plant Types by Fuel")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Power Plants")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

#statistical analysis 
fuel_stats = df.groupby("primary_fuel")[generation_cols].agg(["mean", "median", "std"])
print(fuel_stats)


#Hypothesis testing 
coal_output = df[df["primary_fuel"] == "Coal"][generation_cols].values.flatten()
gas_output = df[df["primary_fuel"] == "Gas"][generation_cols].values.flatten()

# Remove zero values
coal_output = coal_output[coal_output > 0]
gas_output = gas_output[gas_output > 0]

# Perform t-test
t_stat, p_value = ttest_ind(coal_output, gas_output, equal_var=False)
print(f"T-Statistic: {t_stat}, P-Value: {p_value}")


# Grouping by commissioning year to count the number of power plants per year
yearly_trend = df.groupby("commissioning_year")["primary_fuel"].value_counts().unstack(fill_value=0)

# Plotting the trend of power plant establishments over time
plt.figure(figsize=(12, 6))
yearly_trend.sum(axis=1).plot(kind='line', marker='o', linestyle='-', linewidth=2)
plt.title("Number of Power Plants Established Over Time")
plt.xlabel("Year of Commissioning")
plt.ylabel("Number of Power Plants")
plt.grid(True)
plt.show()

# Plotting the evolution of fuel types over the years
yearly_trend.plot(kind='area', stacked=True, alpha=0.6, figsize=(20, 10))
plt.title("Evolution of Power Plant Fuel Types Over Time")
plt.xlabel("Year of Commissioning")
plt.ylabel("Number of Power Plants")
plt.legend(title="Fuel Type", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()

# Scatter plot of power plants' geographical distribution
plt.figure(figsize=(20, 10))
fuel_types = df["primary_fuel"].unique()
colors = sns.color_palette("Set2", len(fuel_types))

# Create a dictionary mapping each fuel type to a color
fuel_color_map = {fuel: color for fuel, color in zip(fuel_types, colors)}

# Scatter plot with different colors for fuel types
for fuel in fuel_types:
    subset = df[df["primary_fuel"] == fuel]
    plt.scatter(subset["longitude"], subset["latitude"], 
                color=fuel_color_map[fuel], label=fuel, alpha=0.6, s=10)

plt.title("Geographical Distribution of Power Plants by Fuel Type")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(title="Fuel Type", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()



# Extract relevant numerical features for matrix operations
matrix_data = df[["capacity_mw", "latitude", "longitude"]].values

# Compute the covariance matrix
cov_matrix = np.cov(matrix_data, rowvar=False)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Display results
print(cov_matrix) 
print(eigenvalues)
print(eigenvectors)
