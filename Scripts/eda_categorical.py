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

# Define categorical features to analyze
categorical_features = ['Brand', 'FuelType', 'Transmission', 'Owner']

# Create subplots for categorical features
fig, axes = plt.subplots(len(categorical_features), 1, figsize=(10, 20))

for i, feature in enumerate(categorical_features):
    # Boxplot for categorical feature vs. AskPrice
    sns.boxplot(data=data, x=feature, y='AskPrice', ax=axes[i])
    axes[i].set_title(f'{feature} vs. AskPrice')
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('AskPrice')
    axes[i].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
