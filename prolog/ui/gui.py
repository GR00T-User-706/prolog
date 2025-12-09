import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

from prolog.manager import classify, start_project
from prolog.utils.jsondb import load_inventory

DB_PATH = Path.home() / "Projects" / ".prolog" / "projects.json"

CATEGORIES = [
    "idea", "started", "in_progress", "working", "finished", "broken"
]


def ask_category():
    dialog = tk.Toplevel()
    dialog.title("Choose Category")
    dialog.geometry("300x150")

    selected = tk.StringVar(value=CATEGORIES[0])

    ttk.Label(dialog, text="Select Category:").pack(pady=5)

    combo = ttk.Combobox(
        dialog,
        values=CATEGORIES,
        textvariable=selected,
        state="readonly",
    )
    combo.pack(pady=5)

    ttk.Button(dialog, text="OK", command=dialog.destroy).pack(pady=10)

    dialog.wait_window()
    return selected.get()


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
            tree.insert(
                "",
                "end",
                values=(
                    proj["id"],
                    proj["name"],
                    proj["category"],
                    proj["status"],
                    proj["path"],
                ),
            )

    def do_classify():
        # Ask what kind of target to classify
        classify_folder = messagebox.askyesno(
            "Classify",
            "Classify a *folder*?\n\nYes = folder\nNo = file",
        )

        if classify_folder:
            path = filedialog.askdirectory(
                initialdir=str(Path.home()),
                title="Select project folder to classify",
            )
        else:
            path = filedialog.askopenfilename(
                initialdir=str(Path.home()),
                title="Select file to classify",
            )

        if not path:
            return  # user cancelled

        cat = ask_category()

        # Right now classify() always moves; later you can add move flags if you want.
        classify(path, cat)
        refresh()

    def do_start():
        start_project()
        refresh()

    ttk.Button(
        frame, text="Refresh", command=refresh
    ).pack(side="left", padx=5, pady=5)
    ttk.Button(
        frame, text="Classify", command=do_classify
    ).pack(side="left", padx=5, pady=5)
    ttk.Button(
        frame, text="Start New", command=do_start
    ).pack(side="left", padx=5, pady=5)

    refresh()
    root.mainloop()
