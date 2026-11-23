#!/usr/bin/env python3
"""Step 5: conflict policy demo - only the authority writes; corrections are new events."""
import sqlite3

con = sqlite3.connect('policy_demo.sqlite')
con.execute('DROP TABLE IF EXISTS events')  # disposable demo DB
con.execute('CREATE TABLE events (seq INTEGER PRIMARY KEY AUTOINCREMENT, '
            'event TEXT NOT NULL, approved_by TEXT NOT NULL)')
AUTHORIZED = {'Registrar'}


def submit(event, who):
    if who not in AUTHORIZED:
        print('REJECTED:', who, 'is not authorized ->', event)
        return
    con.execute('INSERT INTO events(event, approved_by) VALUES(?,?)', (event, who))
    con.commit()
    print('ACCEPTED:', event)


submit('Issue certificate C-002', 'Registrar')
submit('Issue certificate C-999', 'Employer')                   # blocked
submit('Correction: C-002 re-issued as C-002b', 'Registrar')    # new event, history kept
print('Final ledger:')
for row in con.execute('SELECT * FROM events ORDER BY seq'):
    print(' ', row)
con.close()
