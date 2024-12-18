import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Create boxplots for outlier detection
fig, axes = plt.subplots(len(numerical_features), 1, figsize=(10, 15))

for i, feature in enumerate(numerical_features):
    sns.boxplot(data=data, x=feature, ax=axes[i])
    axes[i].set_title(f'Boxplot for {feature}')
    axes[i].set_xlabel(feature)

plt.tight_layout()
plt.show()
