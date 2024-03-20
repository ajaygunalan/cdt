import pandas as pd
import json
import random
import string  
from datetime import datetime, timedelta

def read_csv_data(folder_name):
    csv_files = {
        "TEMP": f"{folder_name}/TEMP.csv",
        "EDA": f"{folder_name}/EDA.csv",
        "BVP": f"{folder_name}/BVP.csv",
        "ACC": f"{folder_name}/ACC.csv",
        "IBI": f"{folder_name}/IBI.csv",
        "HR": f"{folder_name}/HR.csv"
    }

    data = {}

    for key, file_path in csv_files.items():
        try:
            df = pd.read_csv(file_path, header=None)
            if df.empty:  # Check if the dataframe is empty
                continue  # If it's empty, skip this file and continue with the next one
        except pd.errors.EmptyDataError:
            continue  # Also continue if an EmptyDataError is caught

        if key in ["TEMP", "EDA", "BVP", "HR"]:
            initial_time = df.iloc[0, 0]
            sample_rate = df.iloc[1, 0]
            values = df.iloc[2:].values.flatten().tolist()
            data[key] = {
                "initial_time": initial_time,
                "sample_rate": sample_rate,
                "values": values
            }
        elif key == "ACC":
            initial_time = df.iloc[0, 0]
            sample_rate = df.iloc[1, 0]
            values = df.iloc[2:].values.tolist()  # Keep as list of lists to maintain x, y, z grouping
            data[key] = {
                "initial_time": initial_time,
                "sample_rate": sample_rate,
                "values": values
            }
        elif key == "IBI":
            values = df.values.flatten().tolist()
            data[key] = {
                "values": values
            }
    return data

def generate_random_string(length=16):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_user(folder_name):
    user_id = generate_random_string()
    registration_date = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%dT%H:%M:%S")
    name = random.choice(["John", "Jane", "Alex", "Linda", "Mike"])
    surname = random.choice(["Doe", "Smith", "Johnson", "Williams", "Brown"])
    age = random.randint(18, 100)
    gender = random.choice(["Male", "Female"])
    date_of_birth = (datetime.now() - timedelta(days=365*age)).strftime("%Y-%m-%d")
    fiscal_code = user_id
    address = f"{random.randint(100, 999)} Main St"
    phone = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    email = f"{name.lower()}.{surname.lower()}@example.com"
    username = f"{name.lower()}{surname.lower()}{random.randint(10, 99)}"
    password = generate_random_string(12)

    medical_history = {
        "hypertension": random.choice([True, False]),
        "diabetes": random.choice([True, False]),
        "asthma": random.choice([True, False]),
        "arthritis": random.choice([True, False])
    }

    dynamic_data = {'time_duration': duration}  # Initialize dynamic_data with duration first
    dynamic_data.update(read_csv_data(folder_name))  # Then read CSV data and update dynamic_data

    return {
        "user_id": user_id,
        "static_data": {
            "registration_date": registration_date,
            "name": name,
            "surname": surname,
            "age": age,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "fiscal_code": fiscal_code,
            "address": address,
            "phone": phone,
            "email": email,
            "username": username,
            "password": password,
            "medical_history": medical_history
        },
        "dynamic_data": dynamic_data
    }


def main(folder_name, multiple_users=5):
    users = [generate_user(folder_name) for _ in range(multiple_users)]
    data = {"users": users}
    
    output_file_path = f"{folder_name}/users_data.json"
    with open(output_file_path, "w") as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    folder_name = "5"  # Adjust as necessary for your folder name
    duration = "09:06:00-09:07:01"
    multiple_users = 1  # Set this variable as needed
    main(folder_name, multiple_users)
