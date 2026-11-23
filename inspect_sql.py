#!/usr/bin/env python3
"""Step 4/5: inspect the SQL schema and rows created by solution.py."""
import sqlite3
import sys

db = sys.argv[1] if len(sys.argv) > 1 else 'week01_ledger.sqlite'
con = sqlite3.connect(db)
print('Schema (CREATE TABLE):')
print(' ', con.execute("SELECT sql FROM sqlite_master WHERE name='events'").fetchone()[0])
print('Rows (SELECT ... ORDER BY seq):')
for row in con.execute('SELECT seq, event, approved_by FROM events ORDER BY seq'):
    print(' ', row)
con.close()
