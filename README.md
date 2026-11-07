# JSON-Based Log File Analyzer

## Project details
- Subject: Python Programming
- Language: Python 3
- Data format: JSON
- External libraries: None

## Objective
To read application logs stored in a JSON file and analyze them by counting log levels, filtering entries, searching messages, and saving a summary report.

## Files
- `main.py` — the main Python program
- `logs.json` — sample log data
- `PROJECT_REPORT.md` — project report for submission/editing
- `VIVA_QUESTIONS.md` — practice questions and answers
- `FLOWCHART.md` — text flowchart
- `requirements.txt` — no third-party packages are needed

## How to run
1. Install Python 3 if it is not installed.
2. Keep `main.py` and `logs.json` in the same folder.
3. Open a terminal or Command Prompt in that folder.
4. Run: `python main.py`
5. Select an option from the menu. Choose option 5 to generate `analysis_report.txt`.

If your system uses the `py` launcher, run `py main.py`.

## Menu
1. View all logs
2. View log summary
3. Filter logs by level
4. Search logs by message or timestamp
5. Save analysis report
6. Reload the JSON file after editing it
0. Exit

## Important
The program expects a JSON list where every entry has `timestamp`, `level`, and `message`. If the file is missing, malformed, or has entries missing required fields, the program shows an error instead of crashing.
