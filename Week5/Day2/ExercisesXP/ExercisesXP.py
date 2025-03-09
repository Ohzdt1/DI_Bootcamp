#🌟 Exercise 1 : Understanding the problem and Data Collection

import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Get the correct path for the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "diabetes_prediction_dataset.csv")


# Load dataset
df = pd.read_csv(file_path)

# Display basic info about the dataset
print (df.head())
print("\nDataset Overview:")
print(df.info())


# Count positive and negative cases
print("\nDistribution of Diabetes Cases:")
print(df['diabetes'].value_counts())  # Fix: Use 'diabetes' instead of 'Outcome'

# Splitting data into features (X) and target (y)
X = df.drop(columns=['diabetes'])  # Features
y = df['diabetes']  # Target (0 = No Diabetes, 1 = Diabetes)

# Split the dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining Set Size:", X_train.shape)
print("Testing Set Size:", X_test.shape)

#🌟 Exercise 2 : Model Picking and Standardization 
# Which classification model can we use in this problem and why ?
#Logistic Regression	Simple, interpretable, and works well for binary classification


from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Drop categorical columns (gender, smoking_history) since Logistic Regression requires numerical data
df = df.drop(columns=['gender', 'smoking_history'])

# Splitting data into features (X) and target (y)
X = df.drop(columns=['diabetes'])  # Features
y = df['diabetes']  # Target (0 = No Diabetes, 1 = Diabetes)

# Split the dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#🌟 Exercise 3 : Model Training

# Import necessary libraries for model training
from sklearn.metrics import accuracy_score, classification_report

# Initialize the logistic regression model
model = LogisticRegression(random_state=42, max_iter=1000)  # Increased max_iter to ensure convergence

# Train (fit) the model using the standardized training data
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_output = classification_report(y_test, y_pred)

# Display results
print("Model Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report_output)

#🌟 Exercise 4 : Evaluation Metrics
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Step 1: Plot Accuracy Score
plt.figure(figsize=(6, 4))
plt.bar(["Accuracy"], [accuracy], color="blue")
plt.ylim(0, 1)
plt.title("Model Accuracy")
plt.ylabel("Score")
plt.show()

# Step 2: Plot Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["No Diabetes", "Diabetes"],
            yticklabels=["No Diabetes", "Diabetes"])
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()

# Step 3: Extract Precision, Recall, and F1-score
from sklearn.metrics import precision_recall_fscore_support

precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average=None)

# Plot Precision, Recall, and F1-score
metrics = ["Precision", "Recall", "F1-score"]
values_0 = [precision[0], recall[0], f1[0]]
values_1 = [precision[1], recall[1], f1[1]]

x = range(len(metrics))
width = 0.3

plt.figure(figsize=(8, 5))
plt.bar(x, values_0, width, label="No Diabetes (Class 0)", color="blue")
plt.bar([p + width for p in x], values_1, width, label="Diabetes (Class 1)", color="red")
plt.xticks([p + width / 2 for p in x], metrics)
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Precision, Recall, and F1-score")
plt.legend()
plt.show()

# Return values for comment
accuracy, conf_matrix, precision, recall, f1

#🌟 Exercise 5 : Visualizing the performance of our model

import numpy as np

# Selecting two key features for visualization
features = ['HbA1c_level', 'blood_glucose_level']
X_vis = df[features]
y_vis = df['diabetes']

# Standardizing the selected features
scaler_vis = StandardScaler()
X_vis_scaled = scaler_vis.fit_transform(X_vis)

# Training a Logistic Regression model using only these two features
model_vis = LogisticRegression(random_state=42, max_iter=1000)
model_vis.fit(X_vis_scaled, y_vis)

# Creating a mesh grid for visualization
x_min, x_max = X_vis_scaled[:, 0].min() - 1, X_vis_scaled[:, 0].max() + 1
y_min, y_max = X_vis_scaled[:, 1].min() - 1, X_vis_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))

# Predicting values for the mesh grid
Z = model_vis.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plotting the decision boundary
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')

# Overlaying actual data points
sns.scatterplot(x=X_vis_scaled[:, 0], y=X_vis_scaled[:, 1], hue=y_vis, palette={0: "blue", 1: "red"}, alpha=0.6, edgecolor='k')

# Labels and title
plt.xlabel('HbA1c Level (Standardized)')
plt.ylabel('Blood Glucose Level (Standardized)')
plt.title(f'Decision Boundary of Logistic Regression\n Model Accuracy: {accuracy * 100:.2f}%')
plt.legend(title="Diabetes", labels=["No Diabetes (0)", "Diabetes (1)"])
plt.show()


# 🌟 Exercise 6 : ROC Curve

from sklearn import metrics

#define metrics
y_pred_proba = model.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)

#create ROC curve
plt.plot(fpr,tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

#define metrics
y_pred_proba = model.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

#create ROC curve
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()
