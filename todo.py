import json
import sys

DATA_FILE = "todos.json"
FEATURE_PRIORITY = True   # ← Feature Flag (will be removed later)

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
        todo = {"id": len(todos)+1, "text": text, "done": False}
        if FEATURE_PRIORITY and len(sys.argv) > 2 and sys.argv[-1].startswith("p:"):
            todo["priority"] = sys.argv[-1][2:]  # p:high
            text = " ".join(sys.argv[2:-1])
            todo["text"] = text
        todos.append(todo)
        save_todos(todos)
        print(f"✅ Task added JD: {text}")

    elif command == "list":
        for t in todos:
            status = "✅" if t["done"] else "⏳"
            prio = f" [{t.get('priority','')}]" if FEATURE_PRIORITY and "priority" in t else ""
            print(f"{status}{prio} {t['id']}. {t['text']}")

    # ... (done and delete commands remain same)
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
