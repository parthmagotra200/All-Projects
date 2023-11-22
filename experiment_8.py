#AIM: WRITE A PROGRAM TO CONVERT TEMPERATURE TO AND FROM CELSIUS TO FAHRENHIET.
#Conversion from Celsius to Fahrenheit:
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example: Convert Celsius to Fahrenheit
celsius_value = 30  # Replace with the Celsius value you want to convert
fahrenheit_result = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value}°C in Fahrenheit is: {fahrenheit_result}°F")

#Conversion from Fahrenheit to Celsius:
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Example: Convert Fahrenheit to Celsius
fahrenheit_value = 86  # Replace with the Fahrenheit value you want to convert
celsius_result = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value}°F in Celsius is: {celsius_result}°C")