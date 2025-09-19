# daily_reminder.py

print("=== Personal Daily Reminder ===")

# Prompt for a single task
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

# Use if-statement to modify the reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print customized reminder
print("\n" + reminder)



