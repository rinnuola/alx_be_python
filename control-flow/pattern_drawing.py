# pattern_drawing.py

# Ask user for pattern size
size = int(input("Enter the size of the pattern: "))

# Use while loop for rows
row = 0
while row < size:
    # Nested for loop for printing *
    for col in range(size):
        print("*", end="")
    print()  # new line after each row
    row += 1
