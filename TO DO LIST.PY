import json
import os

FILENAME = 'tasks.json'

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=2)

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.\n")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks):
            status = "✔️" if task['done'] else "❌"
            print(f"{i+1}. [{status}] {task['title']}")
    print()

# Add a new task
def add_task(tasks):
    title = input("Enter task: ")
    if title:
        tasks.append({'title': title, 'done': False})
        print("✅ Task added.")

# Mark a task as done
def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]['done'] = True
            print("🎉 Task marked as done.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"🗑️ Task '{removed['title']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("👋 Exiting... Your tasks are saved.")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

# Run the program
if __name__ == "__main__":
    main()
