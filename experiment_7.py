#AIM: CREATE A DATABASE USING LISTS AND TUPLES.
# Example database using lists and tuples
# Each tuple represents a record with information about a person: (ID, Name, Age, Gender)

database = [
    (1, 'Alice', 25, 'Female'),
    (2, 'Bob', 30, 'Male'),
    (3, 'Charlie', 22, 'Male'),
    # Add more records as needed
]

# Function to display all records in the database
def display_database():
    print("ID\tName\tAge\tGender")
    print("-" * 30)
    for record in database:
        print(f"{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}")

# Function to add a new record to the database
def add_record(record):
    database.append(record)
    print("Record added successfully.")

# Display the initial database records
print("Initial Database:")
display_database()

# Adding a new record to the database
new_record = (4, 'Eve', 28, 'Female')  # Change values to add a new record
add_record(new_record)

# Displaying the updated database after adding a new record
print("\nUpdated Database:")
display_database()