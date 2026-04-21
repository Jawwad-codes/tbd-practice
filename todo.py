import json
import sys

DATA_FILE = "todos.json"

def load_todos():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def main():
    todos = load_todos()
    
    if len(sys.argv) < 2:
        print("Usage: python todo.py <add|list|done|delete> [text]")
        return

    command = sys.argv[1]

    if command == "add":
        text = " ".join(sys.argv[2:])
        todos.append({"id": len(todos)+1, "text": text, "done": False})
        save_todos(todos)
        print(f"✅ Added: {text}")

    elif command == "list":
        for t in todos:
            status = "✅" if t["done"] else "⏳"
            print(f"{status} {t['id']}. {t['text']}")

    elif command == "done":
        todo_id = int(sys.argv[2])
        for t in todos:
            if t["id"] == todo_id:
                t["done"] = True
                break
        save_todos(todos)
        print(f"✅ Marked done: {todo_id}")

    elif command == "delete":
        todo_id = int(sys.argv[2])
        todos = [t for t in todos if t["id"] != todo_id]
        save_todos(todos)
        print(f"🗑️  Deleted: {todo_id}")

if __name__ == "__main__":
    main()
