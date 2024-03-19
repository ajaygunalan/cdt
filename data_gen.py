import json
import random
import string
from datetime import datetime, timedelta

def generate_random_string(length=16):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_random_dynamic_data():
    # Simulating some dynamic data generation
    date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
    time = "08:00:00--08:02:00"
    EDA = [round(random.uniform(0, 0.4), 6) for _ in range(100)]
    BVP = [round(random.uniform(-1.0, 1.0), 2) for _ in range(200)]
    Acc = [(random.randint(5, 15), random.randint(5, 15), random.randint(50, 70)) for _ in range(100)]
    HR = [round(random.uniform(60.0, 100.0), 2) for _ in range(100)]
    Temp = [round(random.uniform(33.0, 37.0), 2) for _ in range(100)]
    GPS = [{"latitude": random.randint(1000, 9999), "longitude": random.randint(1000, 9999)} for _ in range(50)]

    return {
        date: [{
            "time": time,
            "EDA(micro Sec)": EDA,
            "BVP": BVP,
            "Acc(g)": Acc,
            "HR(BPM)": HR,
            "Temp(°C)": Temp,
            "GPS": GPS
        }]
    }

def generate_user():
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

    dynamic_data = generate_random_dynamic_data()

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

def main(multiple_users=5):
    users = [generate_user() for _ in range(multiple_users)]
    data = {"users": users}
    
    with open("users_data.json", "w") as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    multiple_users = 5  # You can set this variable as needed
    main(multiple_users)
