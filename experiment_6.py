#AIM: WRITE A PROGRAM TO CREATE A LIST OF STUDENTS RECORDS AND SEARCH A STUDENT RECORD USING DICTIONARY.
# Function to search a student record by ID
def search_student_by_id(student_list, student_id):
    for student in student_list:
        if student['id'] == student_id:
            return student  # Return the student record if found
    return None  # Return None if student ID not found

# Creating a list of student records (each student represented by a dictionary)
students = [
    {'id': 101, 'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'id': 102, 'name': 'Bob', 'age': 21, 'grade': 'B'},
    {'id': 103, 'name': 'Charlie', 'age': 19, 'grade': 'C'},
    # Add more students as needed
]

# Example search for a student record by ID
search_id = 102  # Change this value to search for a different student ID
found_student = search_student_by_id(students, search_id)

if found_student:
    print(f"Student found with ID {search_id}:")
    print("ID:", found_student['id'])
    print("Name:", found_student['name'])
    print("Age:", found_student['age'])
    print("Grade:", found_student['grade'])
else:
    print(f"No student found with ID {search_id}")