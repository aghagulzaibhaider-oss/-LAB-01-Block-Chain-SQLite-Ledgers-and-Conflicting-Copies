# Lab 01 - Required Extension and Viva Answers

## Required extension
A fourth approved event, "Issue certificate C-003", was added to the records list and
`len(rows) == 4` is asserted. The conflict remains: more rows or more copies do not decide
whose data is authoritative.

## Viva
1. **Who can correct the record?**
   The organization designated as authoritative by a documented policy, through authenticated
   and audited corrections (new attributable events, not silent overwrites).
2. **Do multiple copies make a blockchain?**
   No. Replication alone lacks consensus rules, cryptographic ordering and independent validation.
3. **When prefer a registrar database?**
   When there is one trusted issuing authority; conventional transactional storage with audit
   trails is simpler and cheaper.

## Conflict policy
Only an authenticated registrar may issue or revoke; sequence numbers only increase;
corrections are new, attributable events.
