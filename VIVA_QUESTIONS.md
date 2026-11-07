# Viva Questions and Answers

**1. What is the aim of this project?**  
To analyze log entries stored in a JSON file and summarize the different types of events.

**2. What is a log file?**  
A log file stores records of events that happen in a computer program or system.

**3. What is JSON?**  
JSON stands for JavaScript Object Notation. It is a text format used to store and exchange structured data.

**4. Which Python module reads JSON data?**  
The built-in `json` module. `json.load()` reads JSON from an open file.

**5. Why is file handling used?**  
It allows the program to open and read `logs.json` and write the report file.

**6. What is a dictionary in Python?**  
A dictionary stores data as key-value pairs. Each log entry in this project is a dictionary.

**7. What is a list?**  
A list stores multiple items. The JSON array becomes a Python list of log dictionaries.

**8. What are INFO, WARNING, and ERROR?**  
INFO records normal events, WARNING highlights a possible issue, and ERROR records a problem.

**9. Why are functions used?**  
Functions divide the program into smaller parts, making it easier to read, test, and maintain.

**10. What is exception handling?**  
It lets a program respond to errors, such as invalid JSON, without abruptly crashing.

**11. What does `json.JSONDecodeError` mean?**  
It is raised when the file content cannot be decoded as valid JSON.

**12. How does the search feature work?**  
It checks whether the user's keyword appears in a log message or timestamp, ignoring uppercase and lowercase differences.

**13. What is the purpose of `analysis_report.txt`?**  
It stores the generated summary and error details for later review.

**14. Does the project need external packages?**  
No. It uses modules included with Python.

**15. What improvements can be added?**  
Date-range filtering, charts, CSV export, multiple log files, and live log monitoring.
