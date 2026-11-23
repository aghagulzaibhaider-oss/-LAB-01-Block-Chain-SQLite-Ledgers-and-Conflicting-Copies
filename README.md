# Blockchain Lab 01 - SQLite Ledgers and Conflicting Copies

## Purpose
Show that a ledger in a normal database has one authority deciding the official record, and that
extra copies (replication) can disagree with no rule for who is right. The second "ledger" is only
an in-memory Python list - it is NOT a blockchain.

## Files
| File | What it does |
|------|--------------|
| solution.py | Main lab: creates SQLite DB + CSV, inserts 4 events, shows the conflict |
| inspect_sql.py | Prints the table schema and rows from the database |
| conflict_policy_demo.py | Demo of a conflict policy (authority-only writes, corrections as new events) |
| run_on_colab.ipynb | Colab notebook that runs the scripts in order |
| viva_answers.md | Extension answer + 3 viva answers |
| week01_ledger.csv / alternate.csv | Sample CSV outputs |
| expected_output.txt | What the correct output looks like |
| requirements.txt | Dependencies (none - standard library only) |

## How to run (Colab or Linux)
    python3 solution.py
    ls -lh week01_ledger.sqlite week01_ledger.csv
    cat week01_ledger.csv
    python3 solution.py --database alternate.sqlite --export alternate.csv
    python3 inspect_sql.py week01_ledger.sqlite
    python3 conflict_policy_demo.py

In Colab put "!" in front of each command.

## Safety
solution.py runs DROP TABLE on the "events" table. Use disposable database filenames only.

## Submission checklist
Command transcript, code, result table/diagram, three viva answers.
