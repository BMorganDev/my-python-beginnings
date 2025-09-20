# Simple To-Do List App

tasks = []

print("Welcome to your To-Do List App!")

while True:
    print("\nMenu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == "2":
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added!")
    elif choice == "3":
        remove_task = int(input("Enter the task number to remove: "))
        if 0 < remove_task <= len(tasks):
            removed = tasks.pop(remove_task - 1)
            print(f"Task '{removed}' removed!")
        else:
            print("Invalid task number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
