import os

# Define the folder structure
folders = [
    "customer_churn_prediction",
    "customer_churn_prediction/data",
    "customer_churn_prediction/notebooks",
    "customer_churn_prediction/src",
    "customer_churn_prediction/tests"
]

files = {
    "customer_churn_prediction/src": ["__init__.py", "data_loader.py", "eda.py", "preprocess.py", "model.py"],
    "customer_churn_prediction": ["requirements.txt", "README.md", ".gitignore"]
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for folder, filenames in files.items():
    for filename in filenames:
        filepath = os.path.join(folder, filename)
        with open(filepath, "w") as f:
            pass  # Creates an empty file

print("Project structure created successfully!")
