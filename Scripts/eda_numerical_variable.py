import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot theme
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

# Plot distributions of numerical variables
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Distribution of 'Year'
sns.histplot(data['Year'], bins=30, kde=False, ax=axes[0])
axes[0].set_title('Distribution of Car Manufacturing Year')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Frequency')

# Distribution of 'kmDriven'
sns.histplot(data['kmDriven'], bins=30, kde=True, ax=axes[1], color="orange")
axes[1].set_title('Distribution of Kilometers Driven')
axes[1].set_xlabel('Kilometers Driven')
axes[1].set_ylabel('Frequency')

# Distribution of 'AskPrice'
sns.histplot(data['AskPrice'], bins=30, kde=True, ax=axes[2], color="green")
axes[2].set_title('Distribution of Asking Price')
axes[2].set_xlabel('Asking Price')
axes[2].set_ylabel('Frequency')

plt.tight_layout()
plt.show()
