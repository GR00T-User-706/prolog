import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from prolog.manager import list_projects, classify, start_project
from prolog.utils.jsondb import load_inventory
from pathlib import Path

DB_PATH = Path.home() / "Projects" / ".prolog" / "projects.json"


def launch():
    root = tk.Tk()
    root.title("Prolog — Project Catalog GUI")
    root.geometry("700x400")

    frame = ttk.Frame(root)
    frame.pack(fill="both", expand=True)

    columns = ("id", "name", "category", "status", "path")
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=120)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    def refresh():
        tree.delete(*tree.get_children())
        inv = load_inventory(DB_PATH)
        for proj in inv["projects"]:
            tree.insert("", "end", values=(
                proj["id"],
                proj["name"],
                proj["category"],
                proj["status"],
                proj["path"]
            ))

    def do_classify():
        path = simpledialog.askstring("Classify", "Path to classify:")
        cat = simpledialog.askstring("Classify", "Category:")
        if path:
            classify(path, cat)
            refresh()

    def do_start():
        start_project()
        refresh()

    ttk.Button(frame, text="List Projects", command=refresh).pack(side="left", padx=5, pady=5)
    ttk.Button(frame, text="Classify", command=do_classify).pack(side="left", padx=5, pady=5)
    ttk.Button(frame, text="Start New", command=do_start).pack(side="left", padx=5, pady=5)

    refresh()
    root.mainloop()
