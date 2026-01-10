import os

FILE = "to-do-list.txt"

def load():
    data = []
    if os.path.exists(FILE):
        with open(FILE) as f:
            for line in f:
                name, state = line.strip().split("|")
                data.append({"name": name, "state": state})
    return data

def save(data):
    with open(FILE, "w") as f:
        for t in data:
            f.write(t["name"] + "|" + t["state"] + "\n")

def show(data):
    if not data:
        print("\nNo tasks available\n")
        return
    print("\nYour Tasks")
    print("-" * 30)
    for i, t in enumerate(data, 1):
        label = "Completed" if t["state"] == "Done" else "Pending"
        print(f"{i}. {t['name']} ==> {label}")
    print("-" * 30)
    print("Pending:", sum(1 for t in data if t["state"] == "Pending"))

def add(data):
    text = input("New task: ").strip()
    if text:
        data.append({"name": text, "state": "Pending"})
        save(data)
        print("Task added")

def done(data):
    show(data)
    try:
        i = int(input("Task number: ")) - 1
        if 0 <= i < len(data):
            data[i]["state"] = "Done"
            save(data)
            print("Marked as completed")
    except:
        pass

def remove(data):
    show(data)
    try:
        i = int(input("Delete task number: ")) - 1
        if 0 <= i < len(data):
            if input("Confirm (y/n): ").lower() == "y":
                print("Removed:", data.pop(i)["name"])
                save(data)
    except:
        pass

def remove_all(data):
    if not data:
        print("No tasks to delete")
        return
    if input("Are you sure you want to delete ALL tasks? (y/n): ").lower() == "y":
        data.clear()
        save(data)
        print("All tasks deleted")

def main():
    print("\n=== My To-Do List ===")
    tasks = load()
    while True:
        print("\n1.View \n2.Add  \n3.Done  \n4.Delete  \n5.Exit \n6.Delete All Tasks\n")
        ch = input("Choose: ")
        if ch == "1":
            show(tasks)
        elif ch == "2":
            add(tasks)
        elif ch == "3":
            done(tasks)
        elif ch == "4":
            remove(tasks)
        elif ch == "5":
            print("Saved. Bye!")
            break
        elif ch == "6":
            remove_all(tasks)
        else:
            print("Invalid choice")

main()
