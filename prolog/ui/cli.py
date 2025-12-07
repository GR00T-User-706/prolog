 """
CLI helper module for Prolog — mainly delegates to manager functions.
"""
from prolog.manager import classify, start_project, list_projects, open_project

def run_cli():
    print("[CLI MODE]")
    print("1. Classify existing")
    print("2. Start new project")
    print("3. List projects")
    print("4. Open project")
    print("5. Quit")

    while True:
        choice = input("Select option (1-5): ").strip()
        if choice == "1":
            path = input("Enter path: ").strip()
            category = input("Category: ").strip()
            classify(path, category)
        elif choice == "2":
            start_project()
        elif choice == "3":
            list_projects()
        elif choice == "4":
            pid = input("Enter Project ID: ").strip()
            open_project(pid)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
