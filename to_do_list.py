tasks = []

while True:
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            remove = int(input("Enter task number to remove: "))
            tasks.pop(remove - 1)
            print("Task removed!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")

tasks = []

tasks.append({"task": "Revise DT", "done": False})

for task in tasks:
    status = "✓" if task["done"] else "✗"
    print(f"{status} {task['task']}")
