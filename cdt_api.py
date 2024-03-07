import json
from datetime import datetime

def load_data(filename='cdt.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}

def save_data(data, filename='cdt.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def add_user(user_data, filename='cdt.json'):
    data = load_data(filename)
    data['users'].append(user_data)
    save_data(data, filename)

def update_dynamic_data(user_id, date, new_dynamic_data, filename='cdt.json'):
    data = load_data(filename)
    for user in data['users']:
        if user['user_id'] == user_id:
            if date in user['dynamic_data']:
                user['dynamic_data'][date].append(new_dynamic_data)
            else:
                user['dynamic_data'][date] = [new_dynamic_data]
            break
    save_data(data, filename)

def get_user_info(user_id, filename='cdt.json'):
    data = load_data(filename)
    for user in data['users']:
        if user['user_id'] == user_id:
            return user
    return None

# Example usage:

# Adding a new user
new_user = {
    "user_id": "NEWUSR99B07D969M",
    "static_data": {
        "registration_date": "2024-02-11T10:00:00",
        "name": "New",
        "surname": "User",
        "age": 28,
        "gender": "Male",
        "date_of_birth": "1996-05-14",
        "fiscal_code": "NEWUSR99B07D969M",
        "address": "789 Third St",
        "phone": "321-654-9870",
        "email": "new.user@example.com",
        "username": "newuser",
        "password": "encrypted_password",
        "medical_history": {}
    },
    "dynamic_data": {}
}

# Updating dynamic data for an existing user
dynamic_data_for_existing_user = {
    "time": "10:00:00",
    "HR": 76,
    "BP": {"systolic": 116, "diastolic": 74},
    "Temp": 37.1,
    "GPS": {"latitude": 41.40350, "longitude": 2.17410}
}

add_user(new_user)
update_dynamic_data("SMTHAN99A08D123K", "2024-02-11", dynamic_data_for_existing_user)
user_info = get_user_info("DOEJHN99B07D969L")
print("Hi")
print(user_info)