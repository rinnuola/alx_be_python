# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Implement conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
if __name__ == "__main__":
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
        elif unit == "F":
            print(f"{temp}°F is {convert_to_celsius(temp)}°C")
        else:
            print("Invalid unit. Please enter C or F.")
    # Implementation of Value Error
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
