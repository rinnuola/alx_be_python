# multiplication_table.py

# Ask for number input
number = int(input("Enter a number to see its multiplication table: "))

# Generate multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
