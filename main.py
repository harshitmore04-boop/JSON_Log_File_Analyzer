import json
import os
from datetime import datetime

LOG_FILE = "logs.json"
REPORT_FILE = "analysis_report.txt"
VALID_LEVELS = ["INFO", "WARNING", "ERROR"]


def load_logs():
    """Read log entries from the JSON file and return a list."""
    if not os.path.exists(LOG_FILE):
        print(f"\nError: '{LOG_FILE}' was not found.")
        print("Keep logs.json in the same folder as main.py.")
        return None

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            logs = json.load(file)

        if not isinstance(logs, list):
            print("\nError: The JSON file must contain a list of log entries.")
            return None

        # Check that each entry has the required fields.
        for number, log in enumerate(logs, start=1):
            if not isinstance(log, dict) or not all(
                key in log for key in ("timestamp", "level", "message")
            ):
                print(f"\nError: Log entry {number} is missing a required field.")
                print("Each entry must contain timestamp, level, and message.")
                return None

        return logs

    except json.JSONDecodeError:
        print("\nError: logs.json contains invalid JSON.")
        print("Check commas, quotation marks, brackets, and braces.")
        return None
    except OSError as error:
        print(f"\nCould not read the file: {error}")
        return None


def show_logs(logs):
    """Print log entries in a readable format."""
    if not logs:
        print("\nNo log entries found.")
        return

    print("\n" + "=" * 60)
    print("LOG ENTRIES")
    print("=" * 60)
    for number, log in enumerate(logs, start=1):
        print(f"{number}. Time    : {log['timestamp']}")
        print(f"   Level   : {str(log['level']).upper()}")
        print(f"   Message : {log['message']}")
        print("-" * 60)
    print(f"Total entries displayed: {len(logs)}")


def get_summary(logs):
    """Count log entries by level."""
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "OTHER": 0}

    for log in logs:
        level = str(log.get("level", "")).upper()
        if level in VALID_LEVELS:
            counts[level] += 1
        else:
            counts["OTHER"] += 1

    return counts


def show_summary(logs):
    """Display total log count and level counts."""
    counts = get_summary(logs)
    print("\n" + "=" * 40)
    print("LOG SUMMARY")
    print("=" * 40)
    print(f"Total logs       : {len(logs)}")
    print(f"Information logs : {counts['INFO']}")
    print(f"Warnings         : {counts['WARNING']}")
    print(f"Errors           : {counts['ERROR']}")
    print(f"Other levels     : {counts['OTHER']}")

    if counts["ERROR"] > 0:
        print("\nAttention: One or more errors were found.")
    else:
        print("\nNo errors were found.")


def filter_by_level(logs):
    """Show entries matching a level selected by the user."""
    print("\nAvailable levels: INFO, WARNING, ERROR")
    level = input("Enter the level to filter: ").strip().upper()

    if level not in VALID_LEVELS:
        print("Invalid level. Please enter INFO, WARNING, or ERROR.")
        return

    matches = [log for log in logs if str(log.get("level", "")).upper() == level]
    print(f"\nFound {len(matches)} {level} log(s).")
    show_logs(matches)


def search_logs(logs):
    """Search log messages and timestamps for a word or phrase."""
    keyword = input("Enter a word or phrase to search: ").strip().lower()

    if not keyword:
        print("Search text cannot be empty.")
        return

    matches = [
        log for log in logs
        if keyword in str(log.get("message", "")).lower()
        or keyword in str(log.get("timestamp", "")).lower()
    ]

    print(f"\nFound {len(matches)} matching log(s).")
    show_logs(matches)


def save_report(logs):
    """Save a summary and error details to a text file."""
    counts = get_summary(logs)
    lines = [
        "JSON-BASED LOG FILE ANALYZER REPORT",
        "=" * 40,
        f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Source file: {LOG_FILE}",
        "",
        f"Total logs: {len(logs)}",
        f"Information logs: {counts['INFO']}",
        f"Warnings: {counts['WARNING']}",
        f"Errors: {counts['ERROR']}",
        f"Other levels: {counts['OTHER']}",
        "",
        "ERROR DETAILS",
        "=" * 40,
    ]

    errors = [log for log in logs if str(log.get("level", "")).upper() == "ERROR"]
    if errors:
        for log in errors:
            lines.append(f"{log['timestamp']} - {log['message']}")
    else:
        lines.append("No errors found.")

    try:
        with open(REPORT_FILE, "w", encoding="utf-8") as file:
            file.write("\n".join(lines) + "\n")
        print(f"\nReport saved successfully as '{REPORT_FILE}'.")
    except OSError as error:
        print(f"\nCould not save the report: {error}")


def main():
    """Display the menu and process user choices."""
    print("=" * 60)
    print("       JSON-BASED LOG FILE ANALYZER")
    print("=" * 60)

    logs = load_logs()
    if logs is None:
        print("\nProject stopped because the log file could not be loaded.")
        return

    while True:
        print("\nMENU")
        print("1. View all logs")
        print("2. View log summary")
        print("3. Filter logs by level")
        print("4. Search logs")
        print("5. Save analysis report")
        print("6. Reload JSON file")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_logs(logs)
        elif choice == "2":
            show_summary(logs)
        elif choice == "3":
            filter_by_level(logs)
        elif choice == "4":
            search_logs(logs)
        elif choice == "5":
            save_report(logs)
        elif choice == "6":
            updated_logs = load_logs()
            if updated_logs is not None:
                logs = updated_logs
                print("Log file reloaded successfully.")
        elif choice == "0":
            print("Thank you for using the JSON Log File Analyzer.")
            break
        else:
            print("Invalid choice. Please select an option from the menu.")


if __name__ == "__main__":
    main()
