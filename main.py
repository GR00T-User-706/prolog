#!/usr/bin/env python3
"""
Prolog – Unified Project Catalog CLI
"""
import argparse
from prolog.manager import classify, start_project, list_projects, open_project
from prolog.ui import tui, gui

def main():
    parser = argparse.ArgumentParser(
        prog="prolog",
        description="Prolog – Classify, manage, and catalog your projects easily."
    )

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("tui", help="Launch Textual TUI dashboard")
    sub.add_parser("gui", help="Launch Tkinter GUI")
    sub.add_parser("list", help="List all projects")

    classify_cmd = sub.add_parser("classify", help="Classify existing file or directory")
    classify_cmd.add_argument("path", help="Path to file or directory to classify")
    classify_cmd.add_argument(
        "-c", "--category", default="in_progress",
        help="Category for project (idea/started/in_progress/working/finished/broken)"
    )

    sub.add_parser("start", help="Start a new project wizard")

    open_cmd = sub.add_parser("open", help="Open project in Kate by ID")
    open_cmd.add_argument("project_id", help="Project ID")

    args = parser.parse_args()

    if args.command == "tui":
        tui.launch()
    elif args.command == "gui":
        gui.launch()
    elif args.command == "classify":
        classify(args.path, args.category)
    elif args.command == "start":
        start_project()
    elif args.command == "list":
        list_projects()
    elif args.command == "open":
        open_project(args.project_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
