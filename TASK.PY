class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Added task: {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            print(f"Completed task: {self.tasks[index]['task']}")
        else:
            print("Invalid task index")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task index")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "✓" if task['completed'] else "✗"
                print(f"{i}. [{status}] {task['task']}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. List tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task index to complete: "))
            todo_list.complete_task(index)
        elif choice == '3':
            index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(index)
        elif choice == '4':
            todo_list.list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

if _name_ == "_main_":
    main()
