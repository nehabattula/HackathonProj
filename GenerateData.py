import csv
import random
import pandas as pd
from faker import Faker

fake = Faker()

# Generate random data to CSV
def generate_data(num_of_records):
    data = []
    for _ in range(num_of_records):
        customer_id = fake.uuid4()
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = random.randint(18, 75)
        zip_code = fake.zipcode()
        monthly_rent = round(random.uniform(8000, 5000), 2)
        dependent_count = random.randint(0, 5)
        credit_score = random.randint(300, 850)
        credit_limit = round(random.uniform(1000, 20000), 2)
        revolving_credit_balance = round(random.uniform(0, credit_limit), 2)
        estimated_salary = round(random.uniform(20000, 200000), 2)
        account_balance = round(random.uniform(0, 100000), 2)
        months_of_inactivity = random.randint(0, 24)
        
        data.append([
            customer_id, first_name, last_name, age, zip_code, monthly_rent, 
            dependent_count, credit_score, credit_limit, revolving_credit_balance, 
            estimated_salary, account_balance, months_of_inactivity
        ])
    return data

# Write records to a CSV file
def write_to_csv(file_name, data):
    headers = [
        "customer ID", "firstname", "lastname", "age", "zip code", 
        "monthly rent", "dependent count", "credit score", "credit limit", 
        "revolving credit balance", "declared income or estimated salary", 
        "account balance", "months of inactivity"
    ]
    
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# Generate and write records to CSV file
num_of_records = 50000
data = generate_data(num_of_records)
write_to_csv('customer_data2.csv', data)

# New column data
def generate_new_column(num_of_records):
    return [fake.email() for _ in range(num_of_records)]

# Append a new column to csv
def append_new_column(file_name, new_column_name, new_column_data):
    df = pd.read_csv(file_name)
    df[new_column_name] = new_column_data
    df.to_csv(file_name, index=False)

# Data for new column to be appended
new_column_data = generate_new_column(num_of_records)

# Append a new column
append_new_column('customer_data.csv', 'email', new_column_data)