# Decodelab Project 3: SQL Analysis with SQLite & Python
GitHub Repository: https://github.com/seankh06/Decodelabs-Task-3

## Project Objective
Translate business data questions into executable SQL queries by loading the cleaned order dataset into an embedded SQLite database, demonstrating core SQL syntax and aggregate functions.

## SQL Operations Demonstrated
1. Basic `SELECT` row preview & column filtering
2. Conditional row filtering with `WHERE` clause
3. Result sorting with `ORDER BY`
4. Categorical grouping with `GROUP BY`
5. Aggregate calculations: `COUNT()`, `SUM()`, `AVG()` for revenue, order counts, and average spend
6. Yearly revenue trend extraction from date field

## Files Included
1. `Decodelabs Project 3.py` – Python script to build SQLite DB and run all SQL queries


## Tech Stack
- Python (Pandas, sqlite3, openpyxl)
- Embedded SQLite Database (no external server required)
- VS Code IDE
- Git & GitHub Version Control

## How to Run
1. Clone repository
2. Install dependencies: `pip install pandas openpyxl`
3. Execute script: `python "Task-3-SeanKennethH.py"`
4. Script auto-creates SQLite database and prints all SQL query outputs to terminal
