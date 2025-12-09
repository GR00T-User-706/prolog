from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input, Header, Footer, DataTable
from textual.containers import Vertical, Horizontal
from prolog.manager import list_projects, classify, start_project
from prolog.utils.jsondb import load_inventory
from pathlib import Path

DB_PATH = Path.home() / "Projects" / ".prolog" / "projects.json"


class PrologTUI(App):
    CSS_PATH = None
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("🌀 Prolog TUI — Project Catalog", id="title")
        yield Horizontal(
            Button("List Projects", id="list"),
            Button("Classify Path", id="classify"),
            Button("Start New", id="start"),
        )
        self.table = DataTable()
        self.table.add_columns("ID", "Name", "Category", "Status", "Path")
        yield self.table
        yield Footer()

    def on_mount(self):
        self.refresh_table()

    def refresh_table(self):
        self.table.clear()
        inv = load_inventory(DB_PATH)
        for proj in inv["projects"]:
            self.table.add_row(
                proj["id"],
                proj["name"],
                proj["category"],
                proj["status"],
                proj["path"]
            )

    def on_button_pressed(self, event):
        bid = event.button.id
        if bid == "list":
            self.refresh_table()
        elif bid == "classify":
            self.push_screen(ClassifyScreen(self))
        elif bid == "start":
            start_project()
            self.refresh_table()


class ClassifyScreen(App):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def compose(self):
        yield Static("Classify File or Directory")
        self.path_input = Input(placeholder="Enter path...")
        self.cat_input = Input(placeholder="Category (idea/in_progress/...)")
        yield self.path_input
        yield self.cat_input
        yield Button("Submit", id="submit")
        yield Button("Cancel", id="cancel")

    def on_button_pressed(self, event):
        if event.button.id == "submit":
            classify(self.path_input.value, self.cat_input.value)
            self.parent.refresh_table()
            self.exit()
        elif event.button.id == "cancel":
            self.exit()


def launch():
    PrologTUI().run()
