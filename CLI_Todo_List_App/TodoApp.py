def writerTodoFile(todoList, filename='todo.txt'):
    """Writes the current todo list to a file.

    Args:
        todoList (list): The list of todo items to write to the file.
        filename (str): The name of the file to write the todo items to.
    """
    with open(filename, 'w') as file:
        for item in todoList:
            file.write(f"{item}\n")
            print(f"Todo list saved to {filename}.")
    pass

def readerTodoFile(filename='todo.txt'):
    """Reads the todo list from a file.

    Args:
        filename (str): The name of the file to read the todo items from.

    Returns:
        list: The list of todo items read from the file.
    """
    todoList = []
    try:
        with open(filename, 'r') as file:
            todoList = [line.strip() for line in file.readlines()]
        print(f"Todo list loaded from {filename}.")
    except FileNotFoundError:
        print(f"No existing todo file found. Starting with an empty todo list.")
    return todoList

def deleteTodoItem(todoList, itemIndex):
    """Deletes a todo item from the list by its index.

    Args:
        todoList (list): The list of todo items.
        itemIndex (int): The index of the item to delete.
    """
    if 0 <= itemIndex < len(todoList):
        removedItem = todoList.pop(itemIndex)
        print(f"Removed todo item: {removedItem}")
    else:
        print("Invalid index. No item removed.")

def fileToArray(filename='todo.txt'):
    """Reads todo items from a file and returns them as a list.

    Args:
        filename (str): The name of the file to read the todo items from.

    Returns:
        list: The list of todo items read from the file.
    """
    return readerTodoFile(filename)
def main():
    print("Please enter your name:")
    user = input() #sperate input for user name
    print(f"Hello, {user}! Welcome to your Todo List App.")
    todoList =fileToArray() # Load existing todos from file
    while True:
        print("\nMenu:")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Save Todos to File")
        print("4. Delete a Item")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            todo = input("Enter a new todo item: ")
            todoList.append(todo)
            print(f"Added todo: {todo}")
        elif choice == '2':
            print("Your Todo List:")
            for idx, item in enumerate(todoList, start=1):
                print(f"{idx}. {item}")
        elif choice == '3':
            writerTodoFile(todoList)
        elif choice == '4':
            print("Your Todo List:")
            for idx, item in enumerate(todoList, start=1):
                print(f"{idx}. {item}")
            indexToDelete = int(input("Enter the number of the item to delete: ")) - 1
            deleteTodoItem(todoList, indexToDelete)
        elif choice == '5':
            print("Exiting the Todo List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
        
main()