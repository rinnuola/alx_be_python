# daily_reminder.py

print("=== Customized Reminder ===")

# Prompt for a single task
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Process task with match-case
match priority:
    case "high":
        if time_bound == "yes":
            customized_reminder = "is a high priority task that requires immediate attention today!"
        elif time_bound == "no":
            customized_reminder = "is a high priority task. Complete it as soon as possible."
        else:
            print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
            customized_reminder = ""
    case "medium":
        if time_bound == "yes":
            customized_reminder = "is a medium priority task that should be completed soon."
        elif time_bound == "no":
            customized_reminder = "is a medium priority task that can be scheduled later."
        else:
            print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
            customized_reminder = ""
    case "low":
        customized_reminder = "is a low priority task. Consider completing it when you have free time."
    case _:
        print("Invalid priority level entered. Please enter high, medium, or low.")
        customized_reminder = ""

# Displaying the reminder (only if valid)
if customized_reminder:
    print(f"Reminder: '{task}' {customized_reminder}")
