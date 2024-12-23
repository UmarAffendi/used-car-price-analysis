import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Define the path to the dataset
input_path = '../Dataset/cleaned_no_outliers_used_car_dataset.csv'
output_path = '../Dataset/feature_engineered_used_car_dataset.csv'

# Load the dataset
try:
    data = pd.read_csv(input_path)
    print(f"Dataset loaded successfully from {input_path}")
except FileNotFoundError:
    print(f"Error: File not found at {input_path}")
    exit()

# Feature Engineering
print("\nStarting Feature Engineering...")

# 1. Create New Features
data['CarAge'] = 2024 - data['Year']
print("Feature 'CarAge' added.")

# 2. Encode Categorical Variables
categorical_features = ['Brand', 'model', 'FuelType', 'Transmission', 'Owner']
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_features = encoder.fit_transform(data[categorical_features])

# Convert encoded features to a DataFrame
encoded_columns = encoder.get_feature_names_out(categorical_features)
encoded_df = pd.DataFrame(encoded_features, columns=encoded_columns, index=data.index)

# Concatenate encoded features with the original dataset
data = pd.concat([data, encoded_df], axis=1)
data.drop(columns=categorical_features, inplace=True)
print("Categorical features encoded.")

# 3. Normalize/Scale Numerical Features
numerical_features = ['kmDriven', 'CarAge', 'AskPrice']
scaler = StandardScaler()
data[numerical_features] = scaler.fit_transform(data[numerical_features])
print("Numerical features scaled.")

# Save the feature-engineered dataset
data.to_csv(output_path, index=False)
print(f"Feature-engineered dataset saved to {output_path}")
