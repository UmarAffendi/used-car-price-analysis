# Project 2: Used Car Price Analysis

## Overview

This project focuses on analyzing used car data to predict prices and identify market trends. The solution employs machine learning for price prediction, data visualization for insights, and cloud deployment for real-time predictions.


## Features

- **Price Prediction**: Build a regression model using Python to predict used car prices.
- **Market Analysis**: Analyze trends using tools like Power BI to understand price distributions and market demand.
- **Scalability**: Use Databricks for collaborative data preparation and AWS Lambda for deploying the prediction model.


## Tools and Technologies

- **Python**: Pandas, Scikit-learn for data analysis and machine learning.
- **SQL**: Querying and cleaning datasets for analysis.
- **Power BI**: Interactive dashboards to visualize market trends.
- **Databricks**: Collaborative platform for large-scale data preparation and machine learning.
- **AWS Lambda**: Cloud deployment for real-time price predictions.


## Directory Structure

Project-2-Used-Car-Price-Analysis/
│
├── Dataset/
│   └── used_car_dataset.csv
│
├── README.md
└── .gitignore


## How to Run the Project

1. Clone this repository:
```bash
   git clone https://github.com/your-username/Project-2-Used-Car-Price-Analysis.git
   cd used-car-price-analysis
```

2. Set up a Python environment and install dependencies:
```bash
   pip install -r requirements.txt
```

3. Run the Python scripts for data cleaning, analysis, and modeling.

4. Use Power BI to load cleaned data for visualization.

5. Deploy the trained model using AWS Lambda for real-time predictions.


## Dataset
The dataset contains information about used cars, including features like brand, model, year, mileage, and price. The data is stored in the Dataset/ folder.
This dataset is sourced from: https://www.kaggle.com/datasets/mohitkumar282/used-car-dataset


## Future Enhancements
Improve model accuracy by adding advanced feature engineering.
Expand visualizations to include comparative trend analysis.
Optimize deployment pipeline for real-time predictions.