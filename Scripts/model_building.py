import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
import pickle
import os
import matplotlib.pyplot as plt
import numpy as np

# Define the path to the dataset
input_path = '../Dataset/feature_engineered_used_car_dataset.csv'

# Load the dataset
try:
    data = pd.read_csv(input_path)
    print(f"Dataset loaded successfully from {input_path}")
except FileNotFoundError:
    print(f"Error: File not found at {input_path}")
    exit()

# Separate features and target variable
X = data.drop('AskPrice', axis=1)
y = data['AskPrice']

# Check for non-numeric columns in X
non_numeric_columns = X.select_dtypes(include=['object']).columns
print("Non-numeric columns in X:", non_numeric_columns.tolist())

# Split data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print("Data split into training and testing sets.")

# Initialize models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
}

# Dictionary to store evaluation metrics
model_metrics = {}

# Create a directory to save models if it doesn't exist
model_dir = '../models/'
os.makedirs(model_dir, exist_ok=True)

# Train and evaluate each model
for model_name, model in models.items():
    print(f"\nTraining {model_name}...")
    # Train the model
    model.fit(X_train, y_train)
    print(f"{model_name} training completed.")
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = root_mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Store metrics
    model_metrics[model_name] = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'R²': r2
    }
    
    # Save the trained model
    model_path = os.path.join(model_dir, f"{model_name.replace(' ', '_').lower()}.pkl")
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)
    print(f"{model_name} saved to {model_path}")

# Display evaluation metrics for all models
print("\nModel Evaluation Metrics:")
for model_name, metrics in model_metrics.items():
    print(f"\n{model_name}:")
    print(f"Mean Absolute Error (MAE): {metrics['MAE']:.4f}")
    print(f"Mean Squared Error (MSE): {metrics['MSE']:.4f}")
    print(f"Root Mean Squared Error (RMSE): {metrics['RMSE']:.4f}")
    print(f"R-squared (R²): {metrics['R²']:.4f}")


# Assuming Random Forest is the best model
best_model = models['Random Forest']
feature_importances = best_model.feature_importances_

# Create a DataFrame for feature importance
importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': feature_importances
})

# Sort by importance
importance_df = importance_df.sort_values(by='Importance', ascending=False).head(10)

# Plot the top 10 features
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'], color='skyblue')
plt.title('Top 10 Feature Importance (Random Forest)')
plt.xlabel('Importance Score')
plt.ylabel('Features')
plt.gca().invert_yaxis()  # Invert y-axis to have the most important feature at the top
plt.show()