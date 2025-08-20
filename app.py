print("Hello, Fraud Project is ready!")
import csv

# CSV file name
csv_file = "transactions.csv"

# Predefined transactions
transactions = [
    {"Name": "Awwab", "Amount": 500, "Type": "Credit"},
    {"Name": "Ali", "Amount": 200, "Type": "Debit"},
    {"Name": "Sara", "Amount": 300, "Type": "Credit"}
]

# Write transactions to CSV
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ["Name", "Amount", "Type"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for txn in transactions:
        writer.writerow(txn)

print("hello fraud, thing is working")
print(f"Transactions saved to {csv_file}")

# Read and display transactions
print("\nAll Transactions:")
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Amount: {row['Amount']}, Type: {row['Type']}")
# Read and display transactions
print("\nAll Transactions:")
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Amount: {row['Amount']}, Type: {row['Type']}")

# Calculate total credits and debits
total_credit = 0
total_debit = 0

with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = float(row['Amount'])
        if row['Type'].lower() == 'credit':
            total_credit += amount
        elif row['Type'].lower() == 'debit':
            total_debit += amount

print(f"\nTotal Credit: {total_credit}")
print(f"Total Debit: {total_debit}")