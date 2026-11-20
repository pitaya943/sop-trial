<!-- pitaya template 0.1.1 · docs/decisions.md -->
# Decisions

The Owner's decisions. Append only: add a new row, never edit or delete an old one. To change a decision, add a row that supersedes it and name the old number.

A decision that weighed two or more real options and changes the architecture, a public interface or the data model also gets a record in `docs/adr/<nnnn>-<slug>.md` (context, options, decision, consequences); link it from the row's Why. Everything else stays one row.

| # | Date | Decision | Why | Supersedes |
| --- | --- | --- | --- | --- |
| 1 | 2026-11-19 | `split_bill` keeps its error order: type, then people, then amount; tests pin it | Recorded in ticket #6 (/plan Q1); copied here by /setup | |
| 2 | 2026-11-19 | `split_bill` keeps Python's own `TypeError` for missing arguments | Recorded in ticket #6 (/plan Q3); copied here by /setup | |
| 3 | 2026-11-19 | `split_bill` keeps rejecting `int` subclasses (such as `IntEnum`); tests pin it | Recorded in ticket #7 (/plan Q2); copied here by /setup | |
