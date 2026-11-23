#!/usr/bin/env python3
"""Week 01: inspect real SQLite records and disagreements between copies."""
import argparse
import csv
import sqlite3

p = argparse.ArgumentParser()
p.add_argument('--database', default='week01_ledger.sqlite')
p.add_argument('--export', default='week01_ledger.csv')
args = p.parse_args()

# Step 1: create / open the local database file
con = sqlite3.connect(args.database)
con.execute('DROP TABLE IF EXISTS events')  # training data ONLY; use a disposable DB
con.execute('CREATE TABLE events (seq INTEGER PRIMARY KEY, '
            'event TEXT NOT NULL, approved_by TEXT NOT NULL)')

# Four approved events (the 4th is the required extension: C-003)
records = [
    ('Issue certificate C-001', 'Registrar'),
    ('Issue certificate C-002', 'Registrar'),
    ('Revoke certificate C-001', 'Registrar'),   # fixed typo: PDF source had "C001"
    ('Issue certificate C-003', 'Registrar'),    # extension
]
con.executemany('INSERT INTO events(event, approved_by) VALUES(?,?)', records)
con.commit()

# Step 2: read the records back in chronological order
rows = con.execute('SELECT seq, event, approved_by FROM events ORDER BY seq').fetchall()

with open(args.export, 'w', newline='', encoding='utf-8') as output:
    w = csv.writer(output)
    w.writerow(['seq', 'event', 'approved_by'])
    w.writerows(rows)

print('CENTRAL DATABASE (SQLite):')
for r in rows:
    print(' ', r)

# Step 3: two in-memory copies; the employer silently edits event 2
registrar_copy = list(rows)
employer_copy = list(rows)
employer_copy[1] = (employer_copy[1][0], 'Issue certificate C-999', employer_copy[1][2])

print('SHARED-COPY EXPERIMENT (a fourth event does not resolve conflicts):')
for a, b in zip(registrar_copy, employer_copy):
    if a != b:
        print('CONFLICT DETECTED:', a, 'versus', b)
print('Audit question: WHO is authorized to decide the correct record?')

assert len(rows) == 4 and registrar_copy != employer_copy
print('PASS: central ledger stored; independently modified copies disagree.')
con.close()
