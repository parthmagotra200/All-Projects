#AIM: CONSIDER THE STRING "WELCOME TO PYTHON WORLD". PERFORM THE FOLLOWING OPERATIONS: 1) COUNT THE NUMBER OF ALPHABETS IN THE GIVEN STRING. 2) TO EXTRACT CHARACTERS IN THE GIVEN, RANGE FROM THE GIVEN STRING. 3) CHECK IF THE STRING IS ALPHANUMERIC OR NOT. 
#Count the number of alphabets in the given string:
string = "Welcome to Python World"

# Counting the number of alphabets
alphabets_count = sum(c.isalpha() for c in string)
print("Number of alphabets in the string:", alphabets_count)

#Extract characters in the given range from the string:
start_index = 3
end_index = 10

# Extracting characters in the given range
extracted_chars = string[start_index:end_index]
print(f"Characters from index {start_index} to {end_index - 1}: {extracted_chars}")

#Check if the string is alphanumeric or not:

# Check if the string is alphanumeric
is_alphanumeric = string.isalnum()
if is_alphanumeric:
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")