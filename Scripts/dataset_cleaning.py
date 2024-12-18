import pandas as pd

# Load the dataset
file_path = '../Dataset/used_car_dataset.csv'  
used_car_data = pd.read_csv(file_path)

# Clean the 'kmDriven' column
# Remove ' km', ',' and convert to numeric
used_car_data['kmDriven'] = (
    used_car_data['kmDriven']
    .str.replace(' km', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float, errors='ignore')
)

# Clean the 'AskPrice' column
# Remove '₹ ' and ',' and convert to numeric
used_car_data['AskPrice'] = (
    used_car_data['AskPrice']
    .str.replace('₹ ', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float, errors='ignore')
)

# Drop irrelevant or redundant columns
# Columns to drop: 'PostedDate', 'AdditionInfo', 'Age' (not useful for modeling)
columns_to_drop = ['PostedDate', 'AdditionInfo', 'Age']
used_car_data = used_car_data.drop(columns=columns_to_drop)

# Handle missing or invalid numeric values
# Convert 'Year', 'kmDriven', and 'AskPrice' to numeric and drop rows with invalid values
numeric_columns = ['Year', 'kmDriven', 'AskPrice']
used_car_data[numeric_columns] = used_car_data[numeric_columns].apply(pd.to_numeric, errors='coerce')
used_car_data = used_car_data.dropna(subset=numeric_columns)

# Save the cleaned dataset for reuse
cleaned_file_path = '../Dataset/cleaned_used_car_dataset.csv'  # Replace with your file path
used_car_data.to_csv(cleaned_file_path, index=False)

# Display summary of the cleaned dataset
print("Cleaned Data Summary:")
print(used_car_data.describe())
