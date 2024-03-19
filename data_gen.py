import pandas as pd
import json

# Folder name can be specified here
folder_name = "1"

# Define the paths to the CSV files within the specified folder
csv_files = {
    "TEMP": f"{folder_name}/TEMP.csv",
    "EDA": f"{folder_name}/EDA.csv",
    "BVP": f"{folder_name}/BVP.csv",
    "ACC": f"{folder_name}/ACC.csv",
    "IBI": f"{folder_name}/IBI.csv",
    "HR": f"{folder_name}/HR.csv"
}

# Initialize a dictionary to hold the structured data
data = {}

# Process each CSV file
for key, file_path in csv_files.items():
    df = pd.read_csv(file_path, header=None)
    if key in ["TEMP", "EDA", "BVP", "HR"]:  # Files with sample rate
        initial_time = df.iloc[0, 0]
        sample_rate = df.iloc[1, 0]
        values = df.iloc[2:].values.flatten().tolist()  # Flatten and convert to list
        data[key] = {
            "initial_time": initial_time,
            "sample_rate": sample_rate,
            "values": values
        }
    elif key == "ACC":  # ACC has a different structure but handled the same way here
        initial_time = df.iloc[0, 0]
        sample_rate = df.iloc[1, 0]
        values = df.iloc[2:].values.flatten().tolist()  # Flatten and convert to list
        data[key] = {
            "initial_time": initial_time,
            "sample_rate": sample_rate,
            "values": values
        }
    elif key == "IBI":  # IBI does not need a sample rate
        values = df.values.flatten().tolist()  # Flatten and convert to list
        data[key] = {
            "values": values
        }

# Specify the output file path
output_file_path = f"{folder_name}/cdt_1.json"

# Save the structured data to a JSON file
with open(output_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
