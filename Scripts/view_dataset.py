import pandas as pd

# Load the dataset
file_path = '../Dataset/cleaned_no_outliers_used_car_dataset.csv'
data = pd.read_csv(file_path)

# Display the first few rows and column names
print(data.head())
print(data.columns.tolist())