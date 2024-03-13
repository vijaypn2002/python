import json

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = {'title': title, 'description': description, 'completed': False}
        self.tasks.append(task)
        print('Task added successfully!')

    def view_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['title']} - {'(Completed)' if task['completed'] else '(Pending)'}")
                print(f"   Description: {task['description']}")
        else:
            print('No tasks found.')

    def update_task(self, index, title=None, description=None, completed=None):
        if 0 < index <= len(self.tasks):
            task = self.tasks[index - 1]
            if title:
                task['title'] = title
            if description:
                task['description'] = description
            if completed is not None:
                task['completed'] = completed
            print('Task updated successfully!')
        else:
            print('Invalid task index.')

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
            print('Task deleted successfully!')
        else:
            print('Invalid task index.')

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print('File not found.')
        except json.decoder.JSONDecodeError:
            print('Invalid JSON format.')

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to update: "))
            title = input("Enter new title (leave empty to keep unchanged): ")
            description = input("Enter new description (leave empty to keep unchanged): ")
            completed = input("Is the task completed? (yes/no): ").lower()
            if completed == 'yes':
                completed = True
            elif completed == 'no':
                completed = False
            else:
                completed = None
            todo_list.update_task(index, title, description, completed)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            filename = input("Enter filename to save: ")
            todo_list.save_to_file(filename)
            print('Tasks saved to file.')
        elif choice == '6':
            filename = input("Enter filename to load: ")
            todo_list.load_from_file(filename)
            print('Tasks loaded from file.')
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
