# Simple To-Do List App

tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_number = int(input("Enter task number to remove: "))
                removed = tasks.pop(task_number - 1)
                print(f"Removed task: {removed}")
            except:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")