#Create a function max_of_three that takes three numbers as arguments and returns the largest of them and also create a parameter function that checks whether a given number is Armstrong or not.
def max_of_three(num1, num2, num3):
#"Returns the largest of three numbers"
    return max(num1, num2, num3)
def is_armstrong_number(number):
#"Returns True if the given number is an Armstrong number, False otherwise."
# Convert the number to a string to find ots length
    num_str = str(number)
    num_digits= len(num_str)
# Calculate the sum of each digit raised to the power of the number of digit
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
# Check if the sum is wqual to the original number
    return armstrong_sum == number
# Example usage:
    num1 =int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
# Find the maximum of three numbers
    max_value = max_of_three(num1, num2, num3)
    print(f"The maximum of {num1}, {num2}, {num3} is: {max_value}")
# Check if a number is an Armstrong number
    armstrong_num = int(input("Enter number to check Armstrong number: "))
    print(f"{armstrong_num} is Armstrong: {is_armstrong_number(armstrong_num)}")