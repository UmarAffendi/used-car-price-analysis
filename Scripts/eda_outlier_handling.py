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

# Define a function to detect and handle outliers
def handle_outliers(df, column, lower_quantile=0.05, upper_quantile=0.95):
    lower_bound = df[column].quantile(lower_quantile)
    upper_bound = df[column].quantile(upper_quantile)
    print(f'For {column}: Lower Bound = {lower_bound}, Upper Bound = {upper_bound}')
    # Filtering the outliers
    filtered_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return filtered_df

# Handling outliers for numerical features
numerical_features = ['Year', 'kmDriven', 'AskPrice']
for feature in numerical_features:
    print(f"\nAnalyzing outliers for {feature}:")
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data[feature])
    plt.title(f'Boxplot of {feature}')
    plt.show()

    # Handle outliers using quantile-based filtering
    data = handle_outliers(data, feature)
    print(f"Remaining rows after handling outliers in {feature}: {data.shape[0]}")

# Save the filtered dataset
output_path = '../Dataset/cleaned_no_outliers_used_car_dataset.csv'
data.to_csv(output_path, index=False)
print(f"Filtered dataset saved to {output_path}")
