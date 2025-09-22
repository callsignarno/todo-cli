# Todo CLI

A simple command-line todo list app in Python.  
Keep track of your tasks easily using your terminal, with persistent storage in a JSON file.

---

## Features

- Add new tasks
- Mark tasks as done
- Delete tasks
- List all tasks
- Persistent storage with `todos.json`

---

## Installation

1. Clone the repository:

1. Clone the repository:

    ```bash
    git clone https://github.com/callsignarno/todo-cli.git
    cd todo-cli

2. Make sure you have Python 3 installed:

    ```bash
    python --version

3. Run the app:

    ```bash
    python todo.py

---

## Usage

| Command      | Description                           |
| ------------ | ------------------------------------- |
| `add <task>` | Add a new task to the list            |
| `done <num>` | Mark task number `<num>` as completed |
| `del <num>`  | Delete task number `<num>`            |
| `list`       | Show all tasks                        |
| `quit`       | Save tasks and exit the app           |

---

## Example Session

> add Buy groceries
Added: Buy groceries

> add Finish homework
Added: Finish homework

> list
1. [✘] Buy groceries
2. [✘] Finish homework

> done 1
Marked task 1 as done.

> list
1. [✔] Buy groceries
2. [✘] Finish homework

> del 2
Deleted: Finish homework

> quit
Saved & goodbye!

---

## Notes

1. Tasks are stored in todos.json in the same folder as todo.py.

2. For first-time use, if todos.json doesn’t exist, it will be created automatically.

3. To avoid committing personal tasks, todos.json is included in .gitignore.

---

## Future Enhancements

Add priority levels and due dates

Search tasks by keywords

Package as a standalone .exe for Windows users

---





