import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the theme
sns.set_theme(style="whitegrid")

# Define the path to the dataset
file_path = '../Dataset/cleaned_used_car_dataset.csv'

# Load the dataset
try:
    data = pd.read_csv(file_path)
    print(f"Dataset loaded successfully from {file_path}")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit()

# Select numerical features
numerical_features = ['Year', 'kmDriven', 'AskPrice']

# Compute the correlation matrix
correlation_matrix = data[numerical_features].corr()

# Display the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Numerical Features')
plt.show()
