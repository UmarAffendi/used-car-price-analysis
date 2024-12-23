import pandas as pd

# Load the dataset
file_path = '../Dataset/cleaned_no_outliers_used_car_dataset.csv'
output_path = '../Dataset/used_car_visualization.csv'

# Save the dataset
data = pd.read_csv(file_path)
data.to_csv(output_path, index=False)
print(f"Dataset saved for Power BI visualization: {output_path}")
