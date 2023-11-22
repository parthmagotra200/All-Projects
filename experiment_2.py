#AIM: WRITE A PROGRAM TO ILLUSTRATE ITERATION OVER THE LIST AND DICTIONARY
# Iterating over a List
my_list = [1, 2, 3, 4, 5]

print("Iterating over a List:")
for element in my_list:
    print(element)
  
# Iterating over a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("\nIterating over a Dictionary:")
# Iterating over keys
print("Keys:")
for key in my_dict:
    print(key)

# Iterating over values
print("\nValues:")
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
print("\nKey-Value Pairs:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")