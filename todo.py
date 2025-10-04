import json
import os
from datetime import datetime
import platform

# Base directory: next to the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_FILE = os.path.join(BASE_DIR, "todos.json")

def load_todos():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(STORAGE_FILE, "w") as f:
        json.dump(todos, f, indent=2)
    if platform.system()=="Windows":
        os.system(f'attrib +h "{STORAGE_FILE}"')

def show_todos(todos):
    if not todos:
        print("\n[ No tasks yet ]\n")
        return
    print("\nYour tasks:")
    for i, todo in enumerate(todos, 1):
        status = "✔" if todo["done"] else "✘"
        created = todo.get("created", "N/A")
        print(f"{i}. [{status}] {todo['text']} (added: {created})")
    print()

def main():
    todos = load_todos()

    while True:
        print("Commands: add [task], done [num], del [num], list, quit")
        cmd = input("> ").strip()

        if cmd == "quit":
            save_todos(todos)
            print("Saved & goodbye!")
            break

        elif cmd == "list":
            show_todos(todos)

        elif cmd.startswith("add "):
            text = cmd[4:].strip()
            if text:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                todos.append({"text": text, "done": False, "created": timestamp})
                print(f"Added: {text} (added: {timestamp})")
            else:
                print("⚠ Task text can’t be empty.")

        elif cmd.startswith("done "):
            try:
                idx = int(cmd[5:]) - 1
                todos[idx]["done"] = True
                print(f"Marked task {idx+1} as done.")
            except:
                print("⚠ Invalid task number.")

        elif cmd.startswith("del "):
            try:
                idx = int(cmd[4:]) - 1
                removed = todos.pop(idx)
                print(f"Deleted: {removed['text']}")
            except:
                print("⚠ Invalid task number.")

        else:
            print("⚠ Unknown command.")

if __name__ == "__main__":
    main()
