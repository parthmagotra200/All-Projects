#AIM: WRITE A PROGRAM TO DEMONSTRATE TYPE CHECKING OF VARIOUS DATA TYPES AND DEMONSTRATE THE USE OF FOLLOWING BUILT IN FUNCTIONS IN PYTHON: abs(), len(), round(), isalnum(), type()

# Type Checking
data_types = [10, 10.5, "Hello", True, [1, 2, 3], (4, 5, 6), {'a': 1, 'b': 2}, None]

for data in data_types:
    print(f"Data: {data}")
    print(f"Type: {type(data)}")
    print("=" * 20)

# Demonstrating Built-in Functions
# abs() - Returns the absolute value of a number
num = -10
print(f"Absolute value of {num} is {abs(num)}")

# len() - Returns the length of an object
my_list = [1, 2, 3, 4, 5]
print(f"Length of the list: {len(my_list)}")

# min() - Returns the minimum value from a sequence
numbers = [5, 2, 8, 1, 9]
print(f"Minimum value in the list: {min(numbers)}")

# isalnum() - Checks if all characters in a string are alphanumeric
string1 = "Hello123"
string2 = "Hello 123"
print(f"Is '{string1}' alphanumeric? {string1.isalnum()}")
print(f"Is '{string2}' alphanumeric? {string2.isalnum()}")