# daily_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    print()  # Blank line for output clarity

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be handled today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Plan it into your schedule.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority but time-sensitive task. Don’t forget to do it today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority entered. Please use high, medium, or low.")

if __name__ == "__main__":
    main()
