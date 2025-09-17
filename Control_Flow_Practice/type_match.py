
# Demonstrates using match-case to distinguish between integers and strings

# Test values
test_values = [123, "hello", "12abc"]

for value in test_values:
    try:
        # Try converting to integer if it's a string number
        num = int(value)
        match num:
            case int():
                print("You entered an integer:", num)
    except (ValueError, TypeError):
        # If conversion fails, it's treated as a string
        match value:
            case str():
                print("You entered a string:", value)
            case _:
                print("Invalid data type entered.")
