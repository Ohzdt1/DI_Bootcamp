import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Get the correct path for the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "ex2data1.txt")

# Load dataset
df = pd.read_csv(file_path, header=None, names=['Exam1', 'Exam2', 'Admitted'])

# Visualizing the data with a scatter plot
plt.figure(figsize=(10,5))
admitted = df[df['Admitted'] == 1]
not_admitted = df[df['Admitted'] == 0]

plt.scatter(admitted['Exam1'], admitted['Exam2'], color='blue', marker='o', label='Admitted')
plt.scatter(not_admitted['Exam1'], not_admitted['Exam2'], color='red', marker='x', label='Not Admitted')

plt.xlabel("Exam 1 Score")
plt.ylabel("Exam 2 Score")
plt.legend()
plt.title("Exam Scores vs Admission")
plt.show()

# Splitting data into training and testing sets
X = df[['Exam1', 'Exam2']]
y = df['Admitted']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Applying Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Show the plot
plt.show()
