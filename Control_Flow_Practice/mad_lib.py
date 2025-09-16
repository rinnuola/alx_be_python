# Mad lib assignment
# This is a simple mad lib program that takes user input and generates a story based on the input.
print("Welcome to the Mad Libs game!")

# Directly using inputs instead of asking for them
adjective1 = "funny"
adjective2 = "playful"
adjective3 = "golden"
adjective4 = "unforgettable"

# Conditional twist for fun
if adjective3 == "golden":
    lion_description = "a rare and powerful golden lion"
else:
    lion_description = f"a majestic {adjective3} lion"

# Build the story
story = f"""
On a beautiful {adjective1} day, I went to the zoo.
I saw a funny {adjective2} monkey swinging from the trees.
Then, I spotted {lion_description} lounging in the sun.
What a wild and {adjective4} experience!
"""

# Display the final story
print(story)