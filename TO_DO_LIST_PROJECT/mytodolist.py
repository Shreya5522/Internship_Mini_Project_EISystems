import os

TASK_FILE = "todo.txt"


def load_task():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    else:
        return []


def task_save(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

    print("FILE SAVED AT:")
    print(os.path.abspath(TASK_FILE))


def show_menu():
    print("\n------------- TO-DO LIST -------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("--------------------------------------")


def main():
    tasks = load_task()

    while True:
        show_menu()

        c = input("Enter your choice (1-4): ")

        if c == "1":

            if not tasks:
                print("\nNo task found")

            else:
                print("\nYour Tasks:")

                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif c == "2":

            new_task = input("Enter new Task: ")

            if new_task:
                tasks.append(new_task)
                task_save(tasks)

                print("Task Added!")

            else:
                print("Task cannot be empty")

        elif c == "3":

            if not tasks:
                print("No task to delete")

            else:
                print("\nTasks:")

                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

                n = int(input("Enter the number to delete: "))

                if 1 <= n <= len(tasks):
                    tasks.pop(n - 1)
                    task_save(tasks)
                    print("Task deleted")
                else:
                    print("Invalid task number")

        elif c == "4":
            print("Bye")
            break

        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()



